#!/bin/bash

exec_pwd=$(cd $(dirname $0); pwd)

python3 $exec_pwd/../pyscr/csv_to_multi_dirs.py \
    --read_csv_path $HOME/dataset/airsim/sample_data/file_list.csv \
    --target_col_list 1 2 \
    --dir_name_list img label
