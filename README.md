# Semiconductor Layer Builder (C++)

A lightweight, modular C++ library for simulating and stacking III-V semiconductor layers.

## Goal
The goal of this project is to create a robust, extensible C++ library that allows users to define and build semiconductor structures through the deposition of layers. Each layer can be specified with physical parameters such as thickness and refractive index. The tool is intended for use in modeling and preparing inputs for simulation workflows involving III-V materials, including applications in photonics, optoelectronics, and quantum devices.

The library is performance-focused, testable, and benchmarkable, with future plans to support export formats (JSON, CSV) and potentially integrate visualization and Python bindings.

## Features
- Add custom layers with thickness and refractive index
- Print or export layer stacks
- Benchmark and test-ready

## Build
```bash
mkdir build && cd build
cmake ..
make
./examples/example_build_structure
```

## Testing
```bash
ctest
```

## Benchmarking
```bash
./benchmarks/layer_benchmark
```

## Profiling
```bash
./profiling/run_perf.sh
./profiling/run_valgrind.sh
```