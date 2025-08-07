import tkinter as tk
from tkinter import messagebox
import sys
import os

# Add the build directory to the path for iiiv module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'build', 'src')))

from iiiv import Vertex, Face, Solid
import visualize

class App:
    def __init__(self, master):
        self.master = master
        master.title("III-V Semiconductor Layer Builder")

        self.current_z_offset = 0.0
        self.solids_stack = []

        # Input fields
        self.label_x = tk.Label(master, text="X Dimension:")
        self.label_x.grid(row=0, column=0)
        self.entry_x = tk.Entry(master)
        self.entry_x.grid(row=0, column=1)
        self.entry_x.insert(0, "1.0")

        self.label_y = tk.Label(master, text="Y Dimension:")
        self.label_y.grid(row=1, column=0)
        self.entry_y = tk.Entry(master)
        self.entry_y.grid(row=1, column=1)
        self.entry_y.insert(0, "1.0")

        self.label_z = tk.Label(master, text="Thickness (Z):")
        self.label_z.grid(row=2, column=0)
        self.entry_z = tk.Entry(master)
        self.entry_z.grid(row=2, column=1)
        self.entry_z.insert(0, "0.1")

        # Buttons
        self.add_button = tk.Button(master, text="Add Layer", command=self.add_layer)
        self.add_button.grid(row=3, column=0, columnspan=2)

        self.visualize_button = tk.Button(master, text="Visualize Stack", command=self.visualize_stack)
        self.visualize_button.grid(row=4, column=0, columnspan=2)

        self.clear_button = tk.Button(master, text="Clear Stack", command=self.clear_stack)
        self.clear_button.grid(row=5, column=0, columnspan=2)

        # Stack display
        self.stack_label = tk.Label(master, text="Current Stack (0 layers):")
        self.stack_label.grid(row=6, column=0, columnspan=2)
        self.stack_listbox = tk.Listbox(master, height=5)
        self.stack_listbox.grid(row=7, column=0, columnspan=2)

    def add_layer(self):
        try:
            x = float(self.entry_x.get())
            y = float(self.entry_y.get())
            z = float(self.entry_z.get())

            if x <= 0 or y <= 0 or z <= 0:
                messagebox.showerror("Input Error", "Dimensions must be positive.")
                return

            prism_solid = create_rectangular_prism(x, y, z, self.current_z_offset)
            self.solids_stack.append(prism_solid)
            self.stack_listbox.insert(tk.END, f"Layer {len(self.solids_stack)}: {x}x{y}x{z} at Z={self.current_z_offset:.2f}")
            self.current_z_offset += z
            self.stack_label.config(text=f"Current Stack ({len(self.solids_stack)} layers):")

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for dimensions.")

    def visualize_stack(self):
        if not self.solids_stack:
            messagebox.showinfo("Info", "No layers to visualize.")
            return
        visualize.plot_solids(self.solids_stack)

    def clear_stack(self):
        self.solids_stack = []
        self.current_z_offset = 0.0
        self.stack_listbox.delete(0, tk.END)
        self.stack_label.config(text="Current Stack (0 layers):")
        messagebox.showinfo("Cleared", "Stack cleared.")

def create_rectangular_prism(x_dim, y_dim, z_dim, z_offset):
    # Define vertices for a unit cube, then scale and translate
    # Vertices are ordered to ensure consistent face normals (e.g., outward-facing)
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
    # Front face (0,1,2,3) - indices relative to the 8 base vertices
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

    # Note: The Face constructor expects a shared_ptr to a vector of vertices.
    # For simplicity here, we're creating a new list of scaled_vertices for each prism.
    # For a more optimized approach with many prisms, you might manage a single global
    # shared_ptr to all vertices and pass only indices to Face.
    return Solid(scaled_vertices, faces)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()