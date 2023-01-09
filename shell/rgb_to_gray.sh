#!/bin/bash

exec_pwd=$(cd $(dirname $0); pwd)
write_dir_path=$HOME/dataset/airsim/tmp/blured_grayscaled

python3 $exec_pwd/../pyscr/rgb_to_gray.py \
    --read_csv_path $HOME/dataset/airsim/tmp/blured/file_list.csv \
    --target_col 0 \
    --flag_gamma_correction \
    --write_dir_path $write_dir_path

python3 $exec_pwd/../pyscr/file_list_write.py \
    --read_dir_path $write_dir_path \
    --write_csv_name file_list.csv
