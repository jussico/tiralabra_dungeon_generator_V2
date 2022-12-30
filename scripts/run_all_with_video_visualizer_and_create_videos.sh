#!/bin/bash

set -e

# create dirs
mkdir -p video_images/
mkdir -p videos/

# delete possible old files
rm -rf video_images/*
rm -rf videos/*

# run algorithms
python src/main.py 640 512 video 666 dfs dfs silent 1000
python src/main.py 640 512 video 666 dfs bfs silent 1000
python src/main.py 640 512 video 666 dfs dfs_randomized silent 1000
python src/main.py 640 512 video 666 dfs bfs_randomized silent 1000
python src/main.py 640 512 video 666 dfs dijkstra silent 1000
python src/main.py 640 512 video 666 dfs astar silent 1000
# TODO
# python src/main.py 640 512 video 666 dfs astar_jump_point silent 10
python src/main.py 64 50 video 666 dfs memento_random silent 1000 # slow
python src/main.py 640 512 video 666 dfs wall_follower silent 1000

# create videos
root=$(pwd)
cd video_images/
for hakemisto in * ; do
    echo $hakemisto
    cd "$hakemisto"/
        bash "$root/scripts/create_video.sh" "video_images/$hakemisto" "$hakemisto"
        mv *.mp4 ../../videos/
    cd -
done
