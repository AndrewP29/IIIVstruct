import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

import sys
import os

# Add the build directory to the path for iiiv module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'build', 'src')))

from iiiv import Vertex, Face, Solid, Plane

def plot_solids(original_solids):
    fig = plt.figure(figsize=(12, 9))
    ax = fig.add_subplot(111, projection='3d')
    plt.subplots_adjust(left=0.25)

    all_min_x, all_max_x = float('inf'), float('-inf')
    all_min_y, all_max_y = float('inf'), float('-inf')
    all_min_z, all_max_z = float('inf'), float('-inf')

    # --- Data for Original Solids ---
    original_plot_faces = []
    original_plot_normals = []
    original_plot_planes = []
    original_plot_vertices = []

    for solid in original_solids:
        for face_obj in solid.getFaces():
            face_verts = face_obj.getVertices()
            
            # Collect vertices for plotting
            for v in face_verts:
                original_plot_vertices.append(v)

            # Collect faces for plotting
            xs = [v.getX() for v in face_verts]
            ys = [v.getY() for v in face_verts]
            zs = [v.getZ() for v in face_verts]
            verts_for_poly = [list(zip(xs, ys, zs))]
            poly = Poly3DCollection(verts_for_poly, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.5)
            original_plot_faces.append(poly)

            # Collect normals for plotting
            normal = face_obj.getNormal()
            centroid_x = sum(xs) / len(xs)
            centroid_y = sum(ys) / len(ys)
            centroid_z = sum(zs) / len(zs)
            original_plot_normals.append(ax.quiver(centroid_x, centroid_y, centroid_z, 
                                              normal.getX(), normal.getY(), normal.getZ(), 
                                              color='blue', length=0.5, normalize=True))

            # Collect planes for plotting
            plane_obj = face_obj.getPlaneEquation()
            plane_a = plane_obj.getA()
            plane_b = plane_obj.getB()
            plane_c = plane_obj.getC()
            plane_d = plane_obj.getD()

            # Determine the dominant normal component to avoid division by zero
            abs_nx = abs(plane_a)
            abs_ny = abs(plane_b)
            abs_nz = abs(plane_c)

            # Create a meshgrid for the plane
            # We'll use a larger range for the meshgrid to ensure the plane extends beyond the face
            plot_range = 2.0 # Extend 2 units beyond the face's max extent
            
            # Get face AABB for dynamic meshgrid range
            # Note: Face.getAABB() is not available after revert, so using simple min/max of face vertices
            face_min_x = min(xs)
            face_max_x = max(xs)
            face_min_y = min(ys)
            face_max_y = max(ys)
            face_min_z = min(zs)
            face_max_z = max(zs)

            if abs_nz > abs_nx and abs_nz > abs_ny: # Dominant Z (mostly horizontal plane)
                x_grid = np.linspace(face_min_x - plot_range, face_max_x + plot_range, 10)
                y_grid = np.linspace(face_min_y - plot_range, face_max_y + plot_range, 10)
                xx, yy = np.meshgrid(x_grid, y_grid);
                zz = (-plane_a * xx - plane_b * yy - plane_d) / plane_c;
                original_plot_planes.append(ax.plot_surface(xx, yy, zz, alpha=0.1, color='yellow'))
            elif abs_ny > abs_nx and abs_ny > abs_nz: # Dominant Y (mostly XZ plane)
                x_grid = np.linspace(face_min_x - plot_range, face_max_x + plot_range, 10)
                z_grid = np.linspace(face_min_z - plot_range, face_max_z + plot_range, 10)
                xx, zz = np.meshgrid(x_grid, z_grid);
                yy = (-plane_a * xx - plane_c * zz - plane_d) / plane_b;
                original_plot_planes.append(ax.plot_surface(xx, yy, zz, alpha=0.1, color='yellow'))
            elif abs_nx > 1e-9: # Dominant X (mostly YZ plane)
                y_grid = np.linspace(face_min_y - plot_range, face_max_y + plot_range, 10)
                z_grid = np.linspace(face_min_z - plot_range, face_max_z + plot_range, 10)
                yy, zz = np.meshgrid(y_grid, z_grid);
                xx = (-plane_b * yy - plane_c * zz - plane_d) / plane_a;
                original_plot_planes.append(ax.plot_surface(xx, yy, zz, alpha=0.1, color='yellow'))
            else:
                # Handle perfectly vertical planes (e.g., normal.getZ() == 0 and normal.getY() == 0)
                # This case is rare for non-degenerate faces, but good to have a fallback
                print(f"Warning: Could not plot plane for normal {plane_a}, {plane_b}, {plane_c}")

            # Update overall limits
            all_min_x = min(all_min_x, *xs)
            all_max_x = max(all_max_x, *xs)
            all_min_y = min(all_min_y, *ys)
            all_max_y = max(all_max_y, *ys)
            all_min_z = min(all_min_z, *zs)
            all_max_z = max(all_max_z, *zs)

    # --- Data for Projected Solids (manual projection in Python) ---
    projected_plot_faces = []
    projected_plot_vertices = []

    for solid in original_solids:
        for face_obj in solid.getFaces():
            face_verts = face_obj.getVertices()
            projected_face_verts = []
            for v in face_verts:
                # Manually project vertex onto XY plane (z=0)
                projected_face_verts.append(Vertex(v.getX(), v.getY(), 0.0))
            
            # Collect faces for plotting
            xs = [v.getX() for v in projected_face_verts]
            ys = [v.getY() for v in projected_face_verts]
            zs = [v.getZ() for v in projected_face_verts]
            verts_for_poly = [list(zip(xs, ys, zs))]
            poly = Poly3DCollection(verts_for_poly, facecolors='lightgreen', linewidths=1, edgecolors='darkgreen', alpha=.5)
            projected_plot_faces.append(poly)

            # Collect vertices for plotting
            for v in projected_face_verts:
                projected_plot_vertices.append(v)

            # Update overall limits
            all_min_x = min(all_min_x, *xs)
            all_max_x = max(all_max_x, *xs)
            all_min_y = min(all_min_y, *ys)
            all_max_y = max(all_max_y, *ys)
            all_min_z = min(all_min_z, *zs)
            all_max_z = max(all_max_z, *zs)

    # Add all collected elements to the plot
    for poly in original_plot_faces:
        ax.add_collection3d(poly)
    for normal_quiver in original_plot_normals:
        ax.add_artist(normal_quiver)
    for plane_surface in original_plot_planes:
        ax.add_artist(plane_surface)

    for poly in projected_plot_faces:
        ax.add_collection3d(poly)
        poly.set_visible(False) # Initially hidden

    # Plot all unique vertices
    unique_vertices = []
    seen_coords = set()
    for v in original_plot_vertices + projected_plot_vertices:
        coords = (v.getX(), v.getY(), v.getZ())
        if coords not in seen_coords:
            unique_vertices.append(v)
            seen_coords.add(coords)
    
    xs_all = [v.getX() for v in unique_vertices]
    ys_all = [v.getY() for v in unique_vertices]
    zs_all = [v.getZ() for v in unique_vertices]
    p_vertices = ax.scatter(xs_all, ys_all, zs_all, c='k', s=50)

    # Set plot limits dynamically based on all solids
    range_x = all_max_x - all_min_x
    range_y = all_max_y - all_min_y
    range_z = all_max_z - all_min_z

    max_range = max(range_x, range_y, range_z)

    mid_x = (all_min_x + all_max_x) / 2
    mid_y = (all_min_y + all_max_y) / 2
    mid_z = (all_min_z + all_max_z) / 2

    ax.set_xlim([mid_x - max_range / 2, mid_x + max_range / 2])
    ax.set_ylim([mid_y - max_range / 2, mid_y + max_range / 2])
    ax.set_zlim([mid_z - max_range / 2, mid_z + max_range / 2])

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Stacked Semiconductor Layers')

    # Add CheckButtons for toggling visibility
    rax = plt.axes([0.05, 0.4, 0.15, 0.2]) 
    labels = ['Vertices', 'Faces', 'Normals', 'Planes', 'Projected Solids']
    visibility = [True, True, True, True, False] # Projected solids initially hidden
    check = CheckButtons(rax, labels, visibility)

    def func(label):
        if label == 'Vertices':
            p_vertices.set_visible(not p_vertices.get_visible())
        elif label == 'Faces':
            for poly in original_plot_faces:
                poly.set_visible(not poly.get_visible())
        elif label == 'Normals':
            for normal_quiver in original_plot_normals:
                normal_quiver.set_visible(not normal_quiver.get_visible())
        elif label == 'Planes':
            for plane_surface in original_plot_planes:
                plane_surface.set_visible(not plane_surface.get_visible())
        elif label == 'Projected Solids':
            # Toggle visibility of original solids
            for poly in original_plot_faces:
                poly.set_visible(not poly.get_visible())
            # Hide normals and planes for original solids when projected are shown
            for normal_quiver in original_plot_normals:
                normal_quiver.set_visible(False)
            for plane_surface in original_plot_planes:
                plane_surface.set_visible(False)
            
            # Toggle visibility of projected solids (only faces)
            for poly in projected_plot_faces:
                poly.set_visible(not poly.get_visible())
        plt.draw()

    check.on_clicked(func)

    plt.show()

def create_rectangular_prism(x_dim, y_dim, z_dim, z_offset):
    # Define vertices for a unit cube, then scale and translate
    vertices = [
        Vertex(0, 0, 0), # 0
        Vertex(1, 0, 0), # 1
        Vertex(1, 1, 0), # 2
        Vertex(0, 1, 0), # 3
        Vertex(0, 0, 1), # 4
        Vertex(1, 0, 1), # 5
        Vertex(1, 1, 1), # 6
        Vertex(0, 1, 1)  # 7
    ]

    # Scale and translate vertices
    scaled_vertices = []
    for v in vertices:
        scaled_vertices.append(Vertex(v.getX() * x_dim, v.getY() * y_dim, v.getZ() * z_dim + z_offset))
    
    # Define faces (triangles) for a cube, ensuring consistent winding order for normals
    faces = []
    # Front face (0,1,2,3)
    faces.append(Face(scaled_vertices, [0, 1, 2]))
    faces.append(Face(scaled_vertices, [0, 2, 3]))
    # Back face (4,7,6,5)
    faces.append(Face(scaled_vertices, [4, 7, 6]))
    faces.append(Face(scaled_vertices, [4, 6, 5]))
    # Right face (1,5,6,2)
    faces.append(Face(scaled_vertices, [1, 5, 6]))
    faces.append(Face(scaled_vertices, [1, 6, 2]))
    # Left face (0,3,7,4)
    faces.append(Face(scaled_vertices, [0, 3, 7]))
    faces.append(Face(scaled_vertices, [0, 7, 4]))
    # Top face (3,2,6,7)
    faces.append(Face(scaled_vertices, [3, 2, 6]))
    faces.append(Face(scaled_vertices, [3, 6, 7]))
    # Bottom face (0,4,5,1)
    faces.append(Face(scaled_vertices, [0, 4, 5]))
    faces.append(Face(scaled_vertices, [0, 5, 1]))

    return Solid(scaled_vertices, faces)

if __name__ == '__main__':
    solids_to_plot = []
    current_z_offset = 0.0

    # Add a few layers
    solids_to_plot.append(create_rectangular_prism(1.0, 1.0, 0.1, current_z_offset))
    current_z_offset += 0.1
    solids_to_plot.append(create_rectangular_prism(0.8, 0.8, 0.2, current_z_offset))
    current_z_offset += 0.2
    solids_to_plot.append(create_rectangular_prism(1.2, 0.5, 0.15, current_z_offset))

    print(f"Number of solids to plot: {len(solids_to_plot)}")

    plot_solids(solids_to_plot)
