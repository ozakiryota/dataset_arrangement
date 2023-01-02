#!/bin/bash

exec_pwd=$(cd $(dirname $0); pwd)

python3 $exec_pwd/../pyscr/file_list_divider.py \
    --read_csv_path $HOME/dataset/airsim/tmp/file_list.csv \
    --query_col 2 \
    --query_pixel_value 184 145 182 \
    --min_num_query_pixels 5000
