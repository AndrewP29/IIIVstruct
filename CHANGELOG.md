# Changelog

## 2025-08-06

### Project Scaffolding & Automation
- Initialized the project directory structure:
  - `src/lib`
  - `include`
  - `examples`
  - `tests`
  - `benchmarks`
  - `profiling`
- Created the main `README.md` file with the project description and goals.
- Added executable shell scripts for automating common tasks:
  - `run.sh`: To run the main application (via Python bindings).
  - `test.sh`: For running unit tests.
  - `integration.sh`: Placeholder for integration tests.
  - `performance.sh`: For running benchmarks and profiling tools.
- Added a placeholder `python/main.py` script.

### Core C++ Development
- Created the `Vector` class as a foundational 3D vector object.
  - Header: `include/Vector.h`
  - Implementation: `src/lib/Vector.cpp`
- Added a unit test for the `Vector` class to verify its functionality (`tests/test_vector.cpp`).

### Build System
- Configured the project with CMake to manage the build process.
- Created `CMakeLists.txt` files in the root directory, `src/lib`, and `tests`.
- Successfully compiled the `layerlib` library and the `test_vector` executable.

### Verification
- Executed the `./test.sh` script, which successfully built the project and ran the `test_vector` unit test, confirming the `Vector` class is working correctly.
