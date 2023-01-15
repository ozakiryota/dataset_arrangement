#!/bin/bash

image="dataset_arrangement"
tag="latest"

docker build . \
    -t $image:$tag \
    --build-arg cachebust=$(date +%s)
