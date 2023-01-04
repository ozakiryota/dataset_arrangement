#!/bin/bash

exec_pwd=$(cd $(dirname $0); pwd)

python3 $exec_pwd/../pyscr/train_val_split.py \
    --read_csv_path $HOME/dataset/airsim/sample_data/file_list.csv \
    --flag_random \
    --val_rate 0.3
