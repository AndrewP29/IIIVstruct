# Changelog

## 2025-08-06 (Session 2)

### Features & Enhancements
- **Interactive Visualization**: The Python integration test (`python/visualize.py`) now features interactive checkboxes to toggle the visibility of vertices, faces, and the infinite plane in the 3D plot.
- **Plane Representation**: Created a dedicated `Plane` struct in C++ (`include/Plane.h`) to properly represent the `Ax + By + Cz + D = 0` equation, improving code clarity.
- **Robustness**: Implemented a crucial unit test (`test_vertices_on_plane`) to mathematically verify that all vertices of a `Face` correctly lie on the plane it calculates.

### Python Integration
- **Bindings**: Bound the new `Plane` struct and the `Face` class (including `getVertices` and `getPlaneEquation` methods) to Python using `pybind11`.
- **Dependencies**: Added `numpy` to the `python/requirements.txt` file.

### Bug Fixes
- Fixed a C++ compilation error (`unknown type name 'Plane'`) by adding the necessary `#include "Plane.h"` directive in `Face.h`.
- Corrected a Python `ImportError` for `numpy` by adding it to the requirements file.

### Documentation
- **README**: Significantly updated the `README.md` to reflect the current project structure, features, and execution instructions.
- **Changelog**: Maintained this changelog to track progress.

---

## 2025-08-06 (Session 1)

### Project Scaffolding & Automation
- Initialized the project directory structure (`src`, `include`, `tests`, etc.).
- Created shell scripts for automation (`run.sh`, `test.sh`, `integration.sh`).

### Core C++ Development
- Created the `Vector` class (`Vector.h`, `Vector.cpp`).
- Added a unit test for the `Vector` class (`tests/test_vector.cpp`).

### Build System
- Configured the project with CMake.
- Added `pybind11` for Python bindings and enabled Position-Independent Code (`-fPIC`).