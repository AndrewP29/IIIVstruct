# Project TODO

## Code Quality & Robustness
- [x] Add assertions for critical preconditions (e.g., non-collinear vertices).
- [x] Implement comprehensive exception handling for runtime errors (e.g., invalid arguments).

## Core Library (`layerlib`)

### Vertex Class
- [x] Initial implementation (`Vertex.h`, `Vertex.cpp`)
- [x] Unit tests (`test_vertex.cpp`)
- [x] Renamed from `Vector` to `Vertex`.

### Face Class
- [x] Initial implementation (`Face.h`, `Face.cpp`)
- [x] Implement `getPlaneEquation()` method.
- [x] Basic unit tests (`test_face.cpp`).
- [x] Add unit tests for `getPlaneEquation()`.
- [x] Add unit tests for exception handling (e.g., collinear vertices).
- [x] Add unit test to verify vertices lie on the calculated plane.
- [x] Refactor `Face` to use shared vertex list and store explicit normal.
- [x] Implement `invert()` method to flip face normal.
- [x] Add unit test for `invert()` method.

## Python Bindings
- [x] Bind `Vertex` class.
- [x] Bind `Face` class.
- [x] Bind `Plane` struct.

## Visualization (Integration Tests)
- [x] Plot a single `Vertex`.
- [x] Plot a `Face` and its corresponding infinite plane.
- [x] Plot `Face` normal.
- [x] Add interactive toggles for visualization elements.

## Testing Framework
- [x] Integrate Google Test for C++ unit testing.