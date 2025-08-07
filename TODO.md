# Project TODO

## Code Quality & Robustness
- [x] Add assertions for critical preconditions (e.g., non-collinear vertices).
- [x] Implement comprehensive exception handling for runtime errors (e.g., invalid arguments).

## Core Library (`layerlib`)

### Vector Class
- [x] Initial implementation (`Vector.h`, `Vector.cpp`)
- [x] Unit tests (`test_vector.cpp`)

### Face Class
- [x] Initial implementation (`Face.h`, `Face.cpp`)
- [x] Implement `getPlaneEquation()` method.
- [x] Basic unit tests (`test_face.cpp`).
- [x] Add unit tests for `getPlaneEquation()`.
- [x] Add unit tests for exception handling (e.g., collinear vertices).
- [x] Add unit test to verify vertices lie on the calculated plane.

## Python Bindings
- [x] Bind `Vector` class.
- [x] Bind `Face` class.
- [x] Bind `Plane` struct.

## Visualization (Integration Tests)
- [x] Plot a single `Vector`.
- [x] Plot a `Face` and its corresponding infinite plane.
