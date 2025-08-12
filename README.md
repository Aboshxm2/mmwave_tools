# MMWave Tools
Some python tools useful for working with Texas Instruments mmWave Radars

## Tools Overview
### 1. `record.py`
This script records raw data from serial port connected to an mmWave radar device.
Usage: `python record.py <seconds>`

### 2. `mmw_demo_example_script.py`
This script parses raw binary data recorded from the previous script and extracts point cloud as a csv file.
Usage: `python mmw_demo_example_script.py <recorded_data_file>` 
Copyright: This script is © Texas Instruments Incorporated and is included here unaltered under its original license. I am not the author.

### 3. `reply.py`
This script visualize the detected point cloud in 3d frame by frame.
Usage: `python reply.py <point_cloud.csv>`

## 4. `visualize.py`
This script plots the detected points positions over time.
Usage: `python visualize.py <point_cloud.csv>`
