#!/bin/bash

exec_pwd=$(cd $(dirname $0); pwd)

python3 $exec_pwd/../pyscr/rgb_to_gray.py \
    --read_csv_path $HOME/dataset/airsim/sample_data/file_list.csv \
    --target_col 1 \
    --flag_gamma_correction \
    --write_dir_path $HOME/dataset/airsim/sample_data_grayscaled
