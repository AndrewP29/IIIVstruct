#!/bin/bash
# This script will run the performance tests

# Ensure the project is built
if [ ! -d "build" ]; then
    mkdir build
fi

cd build
cmake ..
make

# Run benchmarks
./benchmarks/layer_benchmark

# Run profiling scripts
../profiling/run_perf.sh
../profiling/run_valgrind.sh
