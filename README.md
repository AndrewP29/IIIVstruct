# Semiconductor Layer Builder (C++)

A lightweight, modular C++ library for simulating and stacking III-V semiconductor layers, with Python bindings for rapid prototyping and visualization.

## Goal
The goal of this project is to create a robust, extensible C++ library that allows users to define and build semiconductor structures. The library is designed to be performance-focused, testable, and easily integrated into larger simulation workflows.

## Features
- Core C++ library for defining geometric primitives (Vectors, Faces).
- Python bindings using `pybind11` for easy scripting and integration.
- Interactive 3D visualization of geometric objects using `matplotlib`.
- A suite of shell scripts for automated building, testing, and integration checks.
- Comprehensive unit tests for C++ components.

## Project Structure
```
IIIVstruct/
├── build/                # Build artifacts
├── include/              # C++ public headers (Vector.h, Face.h, etc.)
├── src/                  # C++ source code (lib, bindings)
├── python/               # Python scripts and virtual environment
├── tests/                # C++ unit tests
├── external/             # Third-party libraries (pybind11)
├── run.sh                # Main execution script
├── test.sh               # Runs all C++ unit tests
├── integration.sh        # Runs Python integration tests (visualization)
├── performance.sh        # Placeholder for performance testing
└── CMakeLists.txt        # Main CMake build script
```

## How to Run

### Build & Run C++ Unit Tests
This command compiles the C++ library and runs all unit tests.
```bash
./test.sh
```

### Run Integration & Visualization Test
This command builds the C++ library, creates the Python bindings, sets up a Python virtual environment, and runs the interactive visualization script.
```bash
./integration.sh
```

## Dependencies
- C++ Compiler (supporting C++11)
- CMake
- Python 3
- `matplotlib` & `numpy` (installed automatically by the integration script)
