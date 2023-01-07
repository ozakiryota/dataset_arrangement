#!/bin/bash

exec_pwd=$(cd $(dirname $0); pwd)

python3 $exec_pwd/../pyscr/file_list_write.py \
    --read_dir_path $HOME/dataset/airsim/sample_data \
    --write_csv_name new_file_list.csv
