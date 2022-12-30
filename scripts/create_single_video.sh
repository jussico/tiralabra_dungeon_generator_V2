#!/bin/bash

function setup {
    # create dirs
    mkdir -p video_images/
    mkdir -p videos/

    # delete possible old files
    rm -rf video_images/*
    rm -rf videos/*
}

function create_single_video {
    width=$((1920/10))
    height=$((1080/10))
    echo "width: $width height: $height"
    # run algorithms
    python src/main.py $width $height video 666 dfs dfs silent 100
    # python src/main.py $width $height video 666 dfs dfs silent 10000
    # python src/main.py $width $height video 666 dfs dfs silent 1000

    # create video
    root=$(pwd)
    cd video_images/
    for hakemisto in * ; do
        echo $hakemisto
        cd "$hakemisto"/
            bash "$root/scripts/create_video.sh" "video_images/$hakemisto" "$hakemisto"
            mv *.mp4 ../../videos/
        cd -
    done
    cd $root
}

setup
create_single_video

# mpv videos/*.mp4
