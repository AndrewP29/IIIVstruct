#!/bin/bash
# This script will run the integration tests

# Create a virtual environment if it doesn't exist
if [ ! -d "python/venv" ]; then
    python3 -m venv python/venv
fi

# Activate the virtual environment and install dependencies
source python/venv/bin/activate
pip install -r python/requirements.txt

# Ensure the project is built
if [ ! -d "build" ]; then
    mkdir build
fi

cd build
cmake ..
make
cd ..

# Run the visualization script
python3 python/visualize.py
