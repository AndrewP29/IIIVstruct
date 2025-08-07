# Changelog

## 2025-08-06 (Session 7)

### Python Integration
- **Solid Visualization**: Integrated `Solid` class into `python/visualize.py`.
  - Created a sample cube `Solid` object.
  - Implemented plotting of `Solid` faces using `Poly3DCollection`.
  - Added interactive toggles for `Solid` and `Vertex` visibility.
- **Bindings Update**: Exposed `Solid` class and its `getFaces()` method to Python via `pybind11`.

### Documentation
- Updated `TODO.md` and `CHANGELOG.md` to reflect the new features and completed tasks.

---

## 2025-08-06 (Session 6)

### Core Library Features
- **Solid Class**: Introduced `Solid` class to represent 3D objects composed of `Face` objects.
- **Edge Struct**: Created `Edge` struct to represent an edge by its two vertex indices, used for manifold checks.
- **Manifold Check**: Implemented `isClosed()` method in `Solid` to verify if the object is manifold (each edge shared by exactly two faces).

### Testing
- **New Solid Tests**: Added `test_solid.cpp` with tests for `Solid` creation and `isClosed()` method, including examples of closed and open solids.

### Bug Fixes
- Added `getIndices()` method to `Face` class to allow `Solid` to access face vertex indices for manifold checks.
- Added missing `#include <algorithm>` to `src/lib/Face.cpp` for `std::reverse`.

### Documentation
- Updated `TODO.md` and `CHANGELOG.md` to reflect the new features and completed tasks.

---

## 2025-08-06 (Session 5)

### Core Library Features
- **Face Inversion**: Added `invert()` method to the `Face` class, which reverses the order of vertex indices and recalculates the face normal, effectively flipping its orientation.
- **Normal Calculation Refinement**: Extracted normal calculation into a private `calculateNormal()` helper method in `Face.cpp` to ensure consistency upon construction and inversion.

### Testing
- **New Face Test**: Added `TEST_F(FaceTest, InvertMethodFlipsNormal)` to `tests/test_face.cpp` to verify the correct behavior of the `invert()` method.

### Python Integration
- **Bindings Update**: Exposed the new `invert()` method of the `Face` class to Python via `pybind11`.

### Documentation
- Updated `TODO.md` and `CHANGELOG.md` to reflect the new features and completed tasks.

---

## 2025-08-06 (Session 4)

### Core Library Refactoring
- **Renamed `Vector` to `Vertex`**: To avoid confusion and better reflect its role as a point in space, the `Vector` class has been renamed to `Vertex`. This involved:
  - Renaming `include/Vector.h` to `include/Vertex.h`.
  - Renaming `src/lib/Vector.cpp` to `src/lib/Vertex.cpp`.
  - Renaming `tests/test_vector.cpp` to `tests/test_vertex.cpp`.
  - Updating all C++ code references (`#include`, class names, function signatures).
  - Updating Python bindings (`src/bindings.cpp`).
  - Updating CMake files (`src/lib/CMakeLists.txt`, `tests/CMakeLists.txt`).
  - Updating Python visualization script (`python/visualize.py`).

---

## 2025-08-06 (Session 3)

### Core Library Refactoring
- **Face Class Redesign**: `Face` now references a shared list of `Vertex` objects via indices, enabling efficient representation of solid objects.
- **Explicit Normal**: `Face` constructor now calculates and stores an explicit `normal_` Vertex, accessible via `getNormal()`.

### Testing Framework
- **Google Test Integration**: Replaced custom unit tests with Google Test framework for `Vertex` and `Face` classes, providing detailed test output and robust assertion capabilities.

### Python Integration
- **Updated Bindings**: Modified `pybind11` bindings for `Face` to accommodate the new constructor signature (shared vertex list and indices).
- **Enhanced Visualization**: `python/visualize.py` now plots the `Face` normal and uses the new `Face` constructor.

### Bug Fixes
- Corrected `test_face.cpp` to use non-collinear vertices in `test_vertices_on_plane` to prevent test crashes.

---

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
