#!/bin/bash

exec_pwd=$(cd $(dirname $0); pwd)

python3 $exec_pwd/../pyscr/image_random_overlay.py \
    --read_csv_path $HOME/dataset/airsim/sample_data/file_list.csv \
    --target_col 1 \
    --front_image_dir_path $exec_pwd/../object_image \
    --write_dir_path $HOME/dataset/airsim/sample_data_overlayed \
    --min_front_scale 0.2 \
    --max_front_scale 0.3
