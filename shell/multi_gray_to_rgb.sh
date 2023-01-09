#!/bin/bash

exec_pwd=$(cd $(dirname $0); pwd)
write_dir_path=$HOME/dataset/airsim/tmp/test_A

python3 $exec_pwd/../pyscr/multi_gray_to_rgb.py \
    --read_csv_path_0 $HOME/dataset/airsim/tmp/blured_grayscaled/file_list.csv \
    --target_col_0 0 \
    --read_csv_path_1 $HOME/dataset/airsim/tmp/segmented/file_list.csv \
    --target_col_1 0 \
    --write_dir_path $write_dir_path

python3 $exec_pwd/../pyscr/file_list_write.py \
    --read_dir_path $write_dir_path \
    --write_csv_name file_list.csv
