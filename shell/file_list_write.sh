#!/bin/bash

exec_pwd=$(cd $(dirname $0); pwd)

python3 $exec_pwd/../pyscr/file_list_write.py \
    --dir_list $HOME/dataset/airsim/sample_data/img $HOME/dataset/airsim/sample_data/label \
    --write_csv_path $HOME/dataset/airsim/sample_data/written_file_list.csv
