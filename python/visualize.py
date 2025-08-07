import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Add the build directory to the path
sys.path.append('build/src')

from iiiv import Vertex, Face, Solid

def main():
    # 1. Define the master list of vertices for a cube
    all_vertices = [
        Vertex(0,0,0), # 0
        Vertex(1,0,0), # 1
        Vertex(1,1,0), # 2
        Vertex(0,1,0), # 3
        Vertex(0,0,1), # 4
        Vertex(1,0,1), # 5
        Vertex(1,1,1), # 6
        Vertex(0,1,1)  # 7
    ]

    # 2. Define faces for a cube (12 triangles, 6 faces)
    faces = []
    # Front face (0,1,2,3)
    faces.append(Face(all_vertices, [0, 1, 2]))
    faces.append(Face(all_vertices, [0, 2, 3]))
    # Back face (4,7,6,5)
    faces.append(Face(all_vertices, [4, 7, 6]))
    faces.append(Face(all_vertices, [4, 6, 5]))
    # Right face (1,5,6,2)
    faces.append(Face(all_vertices, [1, 5, 6]))
    faces.append(Face(all_vertices, [1, 6, 2]))
    # Left face (0,3,7,4)
    faces.append(Face(all_vertices, [0, 3, 7]))
    faces.append(Face(all_vertices, [0, 7, 4]))
    # Top face (3,2,6,7)
    faces.append(Face(all_vertices, [3, 2, 6]))
    faces.append(Face(all_vertices, [3, 6, 7]))
    # Bottom face (0,4,5,1)
    faces.append(Face(all_vertices, [0, 4, 5]))
    faces.append(Face(all_vertices, [0, 5, 1]))

    # 3. Create the Solid object
    cube_solid = Solid(all_vertices, faces)
    print(f"Is cube closed? {cube_solid.isClosed()}")

    # 4. Setup the 3D plot
    fig = plt.figure(figsize=(12, 9))
    ax = fig.add_subplot(111, projection='3d')
    plt.subplots_adjust(left=0.25)

    # 5. Plot the elements
    # Plot Solid Faces
    p_solid_faces = []
    for face_obj in cube_solid.getFaces():
        face_verts = face_obj.getVertices()
        xs = [v.getX() for v in face_verts]
        ys = [v.getY() for v in face_verts]
        zs = [v.getZ() for v in face_verts]
        verts_for_poly = [list(zip(xs, ys, zs))]
        poly = Poly3DCollection(verts_for_poly, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.5)
        ax.add_collection3d(poly)
        p_solid_faces.append(poly)

    # Plot Vertices (from the master list)
    xs_all = [v.getX() for v in all_vertices]
    ys_all = [v.getY() for v in all_vertices]
    zs_all = [v.getZ() for v in all_vertices]
    p_vertices = ax.scatter(xs_all, ys_all, zs_all, c='k', s=50, label='Vertices')

    # 6. Set plot limits and labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim([-0.5, 1.5])
    ax.set_ylim([-0.5, 1.5])
    ax.set_zlim([-0.5, 1.5])
    ax.set_title('Interactive Solid Visualization')

    # 7. Add CheckButtons for toggling visibility
    rax = plt.axes([0.05, 0.4, 0.15, 0.15]) # Adjusted position for more buttons
    labels = ['Solid', 'Vertices']
    visibility = [True, True]
    check = CheckButtons(rax, labels, visibility)

    def func(label):
        if label == 'Solid':
            for poly in p_solid_faces:
                poly.set_visible(not poly.get_visible())
        elif label == 'Vertices':
            p_vertices.set_visible(not p_vertices.get_visible())
        plt.draw()

    check.on_clicked(func)

    plt.show()

if __name__ == '__main__':
    main()