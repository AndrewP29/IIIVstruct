import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def plot_solids(solids):
    fig = plt.figure(figsize=(12, 9))
    ax = fig.add_subplot(111, projection='3d')

    all_min_x, all_max_x = float('inf'), float('-inf')
    all_min_y, all_max_y = float('inf'), float('-inf')
    all_min_z, all_max_z = float('inf'), float('-inf')

    for solid in solids:
        for face_obj in solid.getFaces():
            face_verts = face_obj.getVertices()
            xs = [v.getX() for v in face_verts]
            ys = [v.getY() for v in face_verts]
            zs = [v.getZ() for v in face_verts]

            all_min_x = min(all_min_x, *xs)
            all_max_x = max(all_max_x, *xs)
            all_min_y = min(all_min_y, *ys)
            all_max_y = max(all_max_y, *ys)
            all_min_z = min(all_min_z, *zs)
            all_max_z = max(all_max_z, *zs)

            verts_for_poly = [list(zip(xs, ys, zs))]
            poly = Poly3DCollection(verts_for_poly, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.5)
            ax.add_collection3d(poly)

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
    plt.show()

# Remove the direct execution block as it will be called from main.py
# if __name__ == '__main__':
#     main()
