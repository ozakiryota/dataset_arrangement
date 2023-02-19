#!/bin/bash

exec_pwd=$(cd $(dirname $0); pwd)

python3 $exec_pwd/../pyscr/file_list_cols_merge.py \
    --read_parent_csv_path $HOME/dataset/airsim/center_road_south2north_25/merged_file_list.csv \
    --parent_csv_target_col 0 \
    --read_child_csv_path $HOME/dataset/airsim/center_road_south2north_25/segmented/file_list.csv \
    --child_csv_target_col 0 \
    --write_csv_name merged_merged_file_list.csv
