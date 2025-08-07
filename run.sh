#!/bin/bash
# This script will run the main python script that calls the C++ library

# Ensure the C++ library is built
if [ ! -f "build/lib/liblayerlib.so" ]; then
    echo "Library not found. Building..."
    mkdir -p build
    cd build
    cmake ..
    make
    cd ..
fi

# Run the python script
python3 python/main.py
