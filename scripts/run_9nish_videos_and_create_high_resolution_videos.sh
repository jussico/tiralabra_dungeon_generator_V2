#!/bin/bash

set -e

function setup {
    # create dirs
    mkdir -p video_images/
    mkdir -p videos/

    # delete possible old files
    rm -rf video_images/*
    rm -rf videos/*
}

function create_video {
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
    rm -rf video_images/*
}

function create_single_videos {
    width=$((1920/2))
    height=$((1080/2))
    echo "width: $width height: $height"
    # run algorithms
    python src/main.py $width $height video 666 dfs dfs silent 1000
    create_video
    python src/main.py $width $height video 666 dfs bfs silent 1000
    create_video
    python src/main.py $width $height video 666 dfs dfs_randomized silent 1000
    create_video
    python src/main.py $width $height video 666 dfs bfs_randomized silent 1000
    create_video
    python src/main.py $width $height video 666 dfs dijkstra silent 1000
    create_video
    python src/main.py $width $height video 666 dfs astar silent 1000
    create_video
    # TODO
    # python src/main.py $width $height video 666 dfs astar_jump_point silent 10
    # python src/main.py $(($width/10)) $(($height/10)) video 666 dfs memento_random silent 10000 # slow
    # python src/main.py $width $height video 666 dfs memento_random silent 10000000 # too slow
    python src/main.py $width $height video 666 dfs wall_follower silent 1000
    create_video
    python src/main.py $((width/5)) $((height/5)) video 666 dfs memento_random silent 1000000 # ?
    create_video
}

setup
create_single_videos
