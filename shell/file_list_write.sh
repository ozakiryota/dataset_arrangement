#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Error: Usage: ./file_list_write.sh DIR_PATH"
    exit 1
fi

path_first_char=`echo $1 | cut -c 1`
if [ $path_first_char == '/' ] || [ $path_first_char == '~' ]; then
    dir_path=$1
else
    dir_path="$(pwd)/$1"
fi

exec_pwd=$(cd $(dirname $0); pwd)

python3 $exec_pwd/../pyscr/file_list_write.py \
    --read_dir_path $dir_path \
    --write_csv_name file_list.csv
