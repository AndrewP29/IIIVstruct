import sys
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Add the build directory to the path
sys.path.append('build/src')

from iiiv import Vector, Face

def main():
    # 1. Define the vertices for a face
    vertices = [
        Vector(1, 0, 0),
        Vector(0, 1, 0),
        Vector(0, 0, 1)
    ]

    # 2. Create the Face object
    face = Face(vertices)

    # 3. Get the plane equation
    plane = face.getPlaneEquation()
    normal = plane.normal
    d = plane.d

    print(f"Plane Equation: {normal.getX()}x + {normal.getY()}y + {normal.getZ()}z + {d} = 0")

    # 4. Setup the 3D plot
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # 5. Plot the Face (triangle)
    face_verts = face.getVertices()
    verts = [[v.getX(), v.getY(), v.getZ()] for v in face_verts]
    ax.add_collection3d(Poly3DCollection([verts], facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

    # 6. Plot the infinite plane
    # Create a grid of points for the plane
    xx, yy = np.meshgrid(np.linspace(-2, 2, 10), np.linspace(-2, 2, 10))
    
    # Calculate corresponding z values using the plane equation
    # Ax + By + Cz + D = 0  =>  z = (-Ax - By - D) / C
    if abs(normal.getZ()) > 1e-9: # Avoid division by zero
        zz = (-normal.getX() * xx - normal.getY() * yy - d) / normal.getZ()
        ax.plot_surface(xx, yy, zz, alpha=0.2, color='yellow')

    # 7. Set plot limits and labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    ax.set_zlim([-2, 2])
    ax.set_title('Face and its Infinite Plane')
    plt.show()

if __name__ == '__main__':
    main()
