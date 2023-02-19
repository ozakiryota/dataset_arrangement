#!/bin/bash

exec_pwd=$(cd $(dirname $0); pwd)

python3 $exec_pwd/../pyscr/file_list_rows_merge.py \
    --read_parent_csv_path $HOME/dataset/airsim/center_road_south2north_25/file_list.csv \
    --parent_csv_target_col 1 \
    --read_child_csv_path $HOME/dataset/airsim/center_road_south2north_25/overlayed/file_list.csv \
    --child_csv_target_col 0 \
    --write_csv_name merged_file_list.csv
