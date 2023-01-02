#!/bin/bash

exec_pwd=$(cd $(dirname $0); pwd)

python3 $exec_pwd/../pyscr/file_list_maker.py \
    --dir_list $HOME/dataset/airsim/sample/train_A $HOME/dataset/airsim/sample/train_B \
    --write_csv_path $HOME/dataset/airsim/sample/file_list.csv
