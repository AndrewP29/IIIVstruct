import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

import sys
import os

# Add the build directory to the path for iiiv module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'build', 'src')))

from iiiv import Vertex, Face, Solid, Plane

def plot_objects(vertices=None, faces=None, solids=None, planes=None, title="Projection Example"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    all_coords = []

    if vertices:
        for v in vertices:
            ax.scatter(v.getX(), v.getY(), v.getZ(), color='blue', s=50, label='Vertices')
            all_coords.append([v.getX(), v.getY(), v.getZ()])

    if faces:
        for face_obj in faces:
            face_verts = face_obj.getVertices()
            xs = [v.getX() for v in face_verts]
            ys = [v.getY() for v in face_verts]
            zs = [v.getZ() for v in face_verts]
            verts_for_poly = [list(zip(xs, ys, zs))]
            poly = Poly3DCollection(verts_for_poly, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.5)
            ax.add_collection3d(poly)
            all_coords.extend([[v.getX(), v.getY(), v.getZ()] for v in face_verts])

    if solids:
        for solid_obj in solids:
            for face_obj in solid_obj.getFaces():
                face_verts = face_obj.getVertices()
                xs = [v.getX() for v in face_verts]
                ys = [v.getY() for v in face_verts]
                zs = [v.getZ() for v in face_verts]
                verts_for_poly = [list(zip(xs, ys, zs))]
                poly = Poly3DCollection(verts_for_poly, facecolors='green', linewidths=1, edgecolors='darkgreen', alpha=.3)
                ax.add_collection3d(poly)
                all_coords.extend([[v.getX(), v.getY(), v.getZ()] for v in face_verts])

    if planes:
        for plane_obj in planes:
            # Get plane equation components
            plane_a = plane_obj.getA()
            plane_b = plane_obj.getB()
            plane_c = plane_obj.getC()
            plane_d = plane_obj.getD()

            # Create a meshgrid for the plane
            # Determine the dominant normal component to avoid division by zero
            abs_nx = abs(plane_a)
            abs_ny = abs(plane_b)
            abs_nz = abs(plane_c)

            # Define a reasonable range for the plane plot
            plot_range = 5.0
            x_grid = np.linspace(-plot_range, plot_range, 10)
            y_grid = np.linspace(-plot_range, plot_range, 10)
            z_grid = np.linspace(-plot_range, plot_range, 10)

            if abs_nz > abs_nx and abs_nz > abs_ny: # Dominant Z (mostly horizontal plane)
                xx, yy = np.meshgrid(x_grid, y_grid)
                zz = (-plane_a * xx - plane_b * yy - plane_d) / plane_c
                ax.plot_surface(xx, yy, zz, alpha=0.1, color='yellow', label='Projection Plane')
            elif abs_ny > abs_nx and abs_ny > abs_nz: # Dominant Y (mostly XZ plane)
                xx, zz = np.meshgrid(x_grid, z_grid)
                yy = (-plane_a * xx - plane_c * zz - plane_d) / plane_b
                ax.plot_surface(xx, yy, zz, alpha=0.1, color='yellow', label='Projection Plane')
            elif abs_nx > 1e-9: # Dominant X (mostly YZ plane)
                yy, zz = np.meshgrid(y_grid, z_grid)
                xx = (-plane_b * yy - plane_c * zz - plane_d) / plane_a
                ax.plot_surface(xx, yy, zz, alpha=0.1, color='yellow', label='Projection Plane')
            else:
                print(f"Warning: Could not plot plane for normal {plane_a}, {plane_b}, {plane_c}")

    if all_coords:
        all_coords = np.array(all_coords)
        min_vals = np.min(all_coords, axis=0)
        max_vals = np.max(all_coords, axis=0)

        range_x = max_vals[0] - min_vals[0]
        range_y = max_vals[1] - min_vals[1]
        range_z = max_vals[2] - min_vals[2]

        max_range = max(range_x, range_y, range_z, 1.0) # Ensure at least 1.0 range

        mid_x = (min_vals[0] + max_vals[0]) / 2
        mid_y = (min_vals[1] + max_vals[1]) / 2
        mid_z = (min_vals[2] + max_vals[2]) / 2

        ax.set_xlim([mid_x - max_range / 2, mid_x + max_range / 2])
        ax.set_ylim([mid_y - max_range / 2, mid_y + max_range / 2])
        ax.set_zlim([mid_z - max_range / 2, mid_z + max_range / 2])

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(title)
    plt.legend()
    plt.show()

if __name__ == '__main__':
    # --- Example 1: Projecting a Vertex ---
    print("\n--- Projecting a Vertex ---")
    original_vertex = Vertex(1, 2, 3)
    xy_plane = Plane(0, 0, 1, 0) # Z=0 plane
    projected_vertex_xy = original_vertex.project() # Default to XY plane
    projected_vertex_custom = original_vertex.project(xy_plane)

    print(f"Original Vertex: ({original_vertex.getX()}, {original_vertex.getY()}, {original_vertex.getZ()})")
    print(f"Projected onto XY plane (default): ({projected_vertex_xy.getX()}, {projected_vertex_xy.getY()}, {projected_vertex_xy.getZ()})")
    print(f"Projected onto Z=0 plane (custom): ({projected_vertex_custom.getX()}, {projected_vertex_custom.getY()}, {projected_vertex_custom.getZ()})")

    plot_objects(
        vertices=[original_vertex, projected_vertex_xy],
        planes=[xy_plane],
        title="Vertex Projection onto XY Plane"
    )

    # --- Example 2: Projecting a Face ---
    print("\n--- Projecting a Face ---")
    # Define vertices for a simple triangle in 3D space
    master_vertices_face = [
        Vertex(1, 1, 5), 
        Vertex(3, 1, 5), 
        Vertex(2, 3, 5)
    ]
    original_face = Face(master_vertices_face, [0, 1, 2])
    
    # Project onto XY plane (z=0)
    projected_face_xy = original_face.project()

    print(f"Original Face Normal: ({original_face.getNormal().getX()}, {original_face.getNormal().getY()}, {original_face.getNormal().getZ()})")
    print(f"Projected Face Normal (XY): ({projected_face_xy.getNormal().getX()}, {projected_face_xy.getNormal().getY()}, {projected_face_xy.getNormal().getZ()})")

    plot_objects(
        faces=[original_face, projected_face_xy],
        planes=[xy_plane],
        title="Face Projection onto XY Plane"
    )

    # --- Example 3: Projecting a Solid ---
    print("\n--- Projecting a Solid ---")
    # Create a simple rectangular prism (cube)
    def create_cube(size, z_offset):
        vertices = [
            Vertex(0, 0, 0), Vertex(size, 0, 0), Vertex(size, size, 0), Vertex(0, size, 0),
            Vertex(0, 0, size), Vertex(size, 0, size), Vertex(size, size, size), Vertex(0, size, size)
        ]
        # Scale and translate vertices
        scaled_vertices = []
        for v in vertices:
            scaled_vertices.append(Vertex(v.getX(), v.getY(), v.getZ() + z_offset))

        faces = [
            Face(scaled_vertices, [0, 1, 2]), Face(scaled_vertices, [0, 2, 3]), # Bottom
            Face(scaled_vertices, [4, 7, 6]), Face(scaled_vertices, [4, 6, 5]), # Top
            Face(scaled_vertices, [0, 4, 5]), Face(scaled_vertices, [0, 5, 1]), # Front
            Face(scaled_vertices, [3, 2, 6]), Face(scaled_vertices, [3, 6, 7]), # Back
            Face(scaled_vertices, [1, 5, 6]), Face(scaled_vertices, [1, 6, 2]), # Right
            Face(scaled_vertices, [4, 0, 3]), Face(scaled_vertices, [4, 3, 7])  # Left
        ]
        return Solid(scaled_vertices, faces)

    original_solid = create_cube(2, 1) # A 2x2x2 cube, starting at z=1
    projected_solid_xy = original_solid.project() # Project onto XY plane

    print(f"Original Solid (first face normal): ({original_solid.getFaces()[0].getNormal().getX()}, {original_solid.getFaces()[0].getNormal().getY()}, {original_solid.getFaces()[0].getNormal().getZ()})")
    print(f"Projected Solid (first face normal): ({projected_solid_xy.getFaces()[0].getNormal().getX()}, {projected_solid_xy.getFaces()[0].getNormal().getY()}, {projected_solid_xy.getFaces()[0].getNormal().getZ()})")

    plot_objects(
        solids=[original_solid, projected_solid_xy],
        planes=[xy_plane],
        title="Solid Projection onto XY Plane"
    )
