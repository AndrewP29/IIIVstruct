import tkinter as tk
from tkinter import messagebox
import sys
import os

# Add the build directory to the path for iiiv module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'build', 'src')))

from iiiv import Vertex, Face, Solid
import visualize

# This script will contain the python bindings to call the C++ library

print("Python script executed")

if __name__ == "__main__":
    print("Starting GUI...")
    root = tk.Tk()
    app = App(root)
    root.mainloop()