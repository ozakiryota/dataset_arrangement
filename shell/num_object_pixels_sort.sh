#!/bin/bash

exec_pwd=$(cd $(dirname $0); pwd)

python3 $exec_pwd/../pyscr/num_object_pixels_sort.py \
    --read_csv_path $HOME/dataset/airsim/sample_data/file_list.csv \
    --query_col 2 \
    --query_pixel_value 184 145 182 \
    --min_num_query_pixels 5000
