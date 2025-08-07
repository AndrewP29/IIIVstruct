import sys
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Add the build directory to the path
sys.path.append('build/src')

from iiiv import Vector

def plot_vector(v):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.quiver(0, 0, 0, v.getX(), v.getY(), v.getZ())
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.set_zlim([-10, 10])
    plt.show()

if __name__ == '__main__':
    v = Vector(5, 5, 5)
    plot_vector(v)
