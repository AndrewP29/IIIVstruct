cmake_minimum_required(VERSION 3.10)
project(IIIVstruct)

# Enable Position Independent Code for shared libraries
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

# Enable testing
enable_testing()

# Add subdirectories
add_subdirectory(src/lib)
add_subdirectory(examples)
add_subdirectory(tests)
add_subdirectory(benchmarks)
add_subdirectory(profiling)

# Python bindings
add_subdirectory(external/pybind11)
add_subdirectory(src)
