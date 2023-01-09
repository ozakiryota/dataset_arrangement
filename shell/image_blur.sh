#!/bin/bash

exec_pwd=$(cd $(dirname $0); pwd)
write_dir_path=$HOME/dataset/airsim/tmp/blured

python3 $exec_pwd/../pyscr/image_blur.py \
    --read_csv_path $HOME/dataset/airsim/tmp/file_list.csv \
    --target_col 0 \
    --write_dir_path $write_dir_path \
    --blur_radius 30

python3 $exec_pwd/../pyscr/file_list_write.py \
    --read_dir_path $write_dir_path \
    --write_csv_name file_list.csv
