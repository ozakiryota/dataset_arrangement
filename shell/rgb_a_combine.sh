#!/bin/bash

exec_pwd=$(cd $(dirname $0); pwd)

python3 $exec_pwd/../pyscr/rgb_a_combine.py \
    --read_rgb_csv_path $HOME/dataset/airsim/sample_data/file_list.csv \
    --rgb_col 1 \
    --read_a_csv_path $HOME/dataset/airsim/sample_data_gray/file_list_grayscaled.csv \
    --a_col 0 \
    --write_dir_path $HOME/dataset/airsim/sample_data_combined
