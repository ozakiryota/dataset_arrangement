#!/bin/bash

exec_pwd=$(cd $(dirname $0); pwd)

python3 $exec_pwd/../pyscr/multi_gray_to_rgb.py \
    --read_csv_path_0 $HOME/dataset/airsim/sample_data/file_list.csv \
    --target_col_0 1 \
    --read_csv_path_1 $HOME/dataset/airsim/sample_data/file_list.csv \
    --target_col_1 2 \
    --write_dir_path $HOME/dataset/airsim/sample_data_combined
