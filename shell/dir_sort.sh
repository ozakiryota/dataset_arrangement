#!/bin/bash

exec_pwd=$(cd $(dirname $0); pwd)

python3 $exec_pwd/../pyscr/dir_sort.py \
    --read_csv_path $HOME/dataset/airsim/sample_data/file_list.csv \
    --dir_name_list imu img label
