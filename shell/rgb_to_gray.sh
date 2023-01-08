#!/bin/bash

exec_pwd=$(cd $(dirname $0); pwd)

python3 $exec_pwd/../pyscr/rgb_to_gray.py \
    --read_csv_path $HOME/dataset/airsim/center_road_south2north_1000_blured/file_list.csv \
    --target_col 0 \
    --write_dir_path $HOME/dataset/airsim/center_road_south2north_1000_blured_graysclaled
