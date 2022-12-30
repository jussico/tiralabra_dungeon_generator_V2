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

function create_single_videos {
    width=$((1920/4))
    height=$((1080/4))
    # run algorithms
    python src/main.py $width $height video 666 dfs dfs silent 100
    python src/main.py $width $height video 666 dfs bfs silent 100
    python src/main.py $width $height video 666 dfs dfs_randomized silent 100
    python src/main.py $width $height video 666 dfs bfs_randomized silent 100
    break
    python src/main.py $width $height video 666 dfs dijkstra silent 1000
    python src/main.py $width $height video 666 dfs astar silent 1000
    # TODO
    # python src/main.py $width $height video 666 dfs astar_jump_point silent 10
    python src/main.py $(($width/10)) $(($height/10)) video 666 dfs memento_random silent 1000 # slow
    python src/main.py $width $height video 666 dfs wall_follower silent 1000

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
}

function create_4x4_video {
    cd videos
    file1=$(ls *-bfs_*)
    file2=$(ls *-dfs2*)
    file3=$(ls *-bfs_*)
    file4=$(ls *-bfs2*)
    # echo $file1 $file2 $file3 $file4
    ffmpeg \
        -i $file1 -i $file2 -i $file3 -i $file4 \
        -filter_complex " \
            nullsrc=size=640x480 [base]; \
            [0:v] setpts=PTS-STARTPTS, scale=320x240 [upperleft]; \
            [1:v] setpts=PTS-STARTPTS, scale=320x240 [upperright]; \
            [2:v] setpts=PTS-STARTPTS, scale=320x240 [lowerleft]; \
            [3:v] setpts=PTS-STARTPTS, scale=320x240 [lowerright]; \
            [base][upperleft] overlay=shortest=1 [tmp1]; \
            [tmp1][upperright] overlay=shortest=1:x=320 [tmp2]; \
            [tmp2][lowerleft] overlay=shortest=1:y=240 [tmp3]; \
            [tmp3][lowerright] overlay=shortest=1:x=320:y=240 \
        " \
        -c:v libx264 4x4_video.mkv    
}

setup
create_single_videos
create_4x4_video



