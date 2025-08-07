cmake_minimum_required(VERSION 3.10)
project(IIIVstruct)

# Enable testing
enable_testing()

# Add subdirectories
add_subdirectory(src/lib)
add_subdirectory(examples)
add_subdirectory(tests)
add_subdirectory(benchmarks)
add_subdirectory(profiling)
