#!/bin/bash

root=$(pwd)

cd video_images/

for hakemisto in * ; do
    echo $hakemisto
    cd "$hakemisto"/
        bash "$root/scripts/create_video.sh" "video_images/$hakemisto" "$hakemisto"
    cd -
    exit(0)
done
