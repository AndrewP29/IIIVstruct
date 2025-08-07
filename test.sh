#!/bin/bash
# This script will run the unit tests

# Ensure the project is built
if [ ! -d "build" ]; then
    mkdir build
fi

cd build
cmake ..
make
ctest
