import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Add the build directory to the path
sys.path.append('build/src')

from iiiv import Vertex, Face

def main():
    # 1. Define the master list of vertices
    all_vertices = [
        Vertex(1, 2, 0),  # Index 0
        Vertex(0, 1, 2),  # Index 1
        Vertex(2, 0, 1),  # Index 2
        Vertex(0, 0, 0)   # Index 3 (e.g., for origin)
    ]

    # 2. Define the indices for a face from the master list
    face_indices = [0, 1, 2] # Using vertices at index 0, 1, 2

    # 3. Create the Face object and get its properties
    face = Face(all_vertices, face_indices)
    plane = face.getPlaneEquation()
    normal = plane.normal
    d = plane.d

    print(f"Face Normal: ({normal.getX()}, {normal.getY()}, {normal.getZ()})")
    print(f"Plane Equation: {normal.getX()}x + {normal.getY()}y + {normal.getZ()}z + {d} = 0")

    # 4. Setup the 3D plot
    fig = plt.figure(figsize=(12, 9))
    ax = fig.add_subplot(111, projection='3d')
    plt.subplots_adjust(left=0.25)

    # 5. Plot the elements
    # Plot Vertices
    face_verts = face.getVertices()
    xs = [v.getX() for v in face_verts]
    ys = [v.getY() for v in face_verts]
    zs = [v.getZ() for v in face_verts]
    p_vertices = ax.scatter(xs, ys, zs, c='k', s=50, label='Vertices')

    # Plot Face
    verts_for_poly = [list(zip(xs, ys, zs))]
    p_face = Poly3DCollection(verts_for_poly, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.5)
    ax.add_collection3d(p_face)

    # Plot Normal (from the centroid of the face)
    centroid_x = sum(xs) / len(xs)
    centroid_y = sum(ys) / len(ys)
    centroid_z = sum(zs) / len(zs)
    p_normal = ax.quiver(centroid_x, centroid_y, centroid_z, 
                         normal.getX(), normal.getY(), normal.getZ(), 
                         color='blue', length=1.0, normalize=True, label='Normal')

    # Plot Plane
    xx, yy = np.meshgrid(np.linspace(-3, 3, 10), np.linspace(-3, 3, 10))
    
    # Handle cases where normal.getZ() is zero (vertical or horizontal plane)
    if abs(normal.getZ()) > 1e-9: 
        zz = (-normal.getX() * xx - normal.getY() * yy - d) / normal.getZ()
        p_plane = ax.plot_surface(xx, yy, zz, alpha=0.2, color='yellow', label='Infinite Plane')
    elif abs(normal.getY()) > 1e-9: # Plane parallel to YZ
        yy_plane = (-normal.getX() * xx - normal.getZ() * zz - d) / normal.getY()
        p_plane = ax.plot_surface(xx, yy_plane, zz, alpha=0.2, color='yellow', label='Infinite Plane')
    elif abs(normal.getX()) > 1e-9: # Plane parallel to XZ
        xx_plane = (-normal.getY() * yy - normal.getZ() * zz - d) / normal.getX()
        p_plane = ax.plot_surface(xx_plane, yy, zz, alpha=0.2, color='yellow', label='Infinite Plane')
    else:
        p_plane = None # Should not happen with valid normal

    # 6. Set plot limits and labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim([-3, 3])
    ax.set_ylim([-3, 3])
    ax.set_zlim([-3, 3])
    ax.set_title('Interactive Face Visualization')

    # 7. Add CheckButtons for toggling visibility
    rax = plt.axes([0.05, 0.4, 0.15, 0.2]) # Adjusted position for more buttons
    labels = ['Vertices', 'Face', 'Normal', 'Plane']
    visibility = [True, True, True, True]
    check = CheckButtons(rax, labels, visibility)

    def func(label):
        if label == 'Vertices':
            p_vertices.set_visible(not p_vertices.get_visible())
        elif label == 'Face':
            p_face.set_visible(not p_face.get_visible())
        elif label == 'Normal':
            p_normal.set_visible(not p_normal.get_visible())
        elif label == 'Plane' and p_plane:
            p_plane.set_visible(not p_plane.get_visible())
        plt.draw()

    check.on_clicked(func)

    plt.show()

if __name__ == '__main__':
    main()
