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
    cd $root
}

# still works but never stops..
function create_2x2_video {
    cd videos
    file1=$(ls *-dfs_*)
    file2=$(ls *-dfs2*)
    file3=$(ls *-bfs_*)
    file4=$(ls *-bfs2*)
    echo $file1 $file2 $file3 $file4
    leveys=$((1920/4))
    korkeus=$((1080/4))
    koko_leveys=$((1920/2))
    koko_korkeus=$((1080/2))
    echo "leveys: ${leveys} korkeus: ${korkeus}"
    ffmpeg \
        -i $file1 -i $file2 -i $file3 -i $file4 \
        -filter_complex " \
            nullsrc=size=${koko_leveys}x${koko_korkeus} [base]; \
            [0:v] setpts=PTS-STARTPTS, scale=${leveys}x${korkeus} [upperleft]; \
            [1:v] setpts=PTS-STARTPTS, scale=${leveys}x${korkeus} [upperright]; \
            [2:v] setpts=PTS-STARTPTS, scale=${leveys}x${korkeus} [lowerleft]; \
            [3:v] setpts=PTS-STARTPTS, scale=${leveys}x${korkeus} [lowerright]; \
            [base][upperleft] overlay=[tmp1]; \
            [tmp1][upperright] overlay=x=${leveys} [tmp2]; \
            [tmp2][lowerleft] overlay=y=${korkeus} [tmp3]; \
            [tmp3][lowerright] overlay=x=${leveys}:y=${korkeus} \
        " \
        -c:v libx264 \
        -shortest 2x2_video.mkv    
}

# works but never stops..
function create_2x2_video {
    cd videos
    file1=$(ls *-dfs_*)
    file2=$(ls *-dfs2*)
    file3=$(ls *-bfs_*)
    file4=$(ls *-bfs2*)
    echo $file1 $file2 $file3 $file4
    leveys=$((1920/4))
    korkeus=$((1080/4))
    koko_leveys=$((1920/2))
    koko_korkeus=$((1080/2))
    echo "leveys: ${leveys} korkeus: ${korkeus}"
    ffmpeg \
        -i $file1 -i $file2 -i $file3 -i $file4 \
        -stream_loop -1 -i $file1 \
        -filter_complex " \
            nullsrc=size=${koko_leveys}x${koko_korkeus} [base]; \
            [0:v] setpts=PTS-STARTPTS, scale=${leveys}x${korkeus} [upperleft]; \
            [1:v] setpts=PTS-STARTPTS, scale=${leveys}x${korkeus} [upperright]; \
            [2:v] setpts=PTS-STARTPTS, scale=${leveys}x${korkeus} [lowerleft]; \
            [3:v] setpts=PTS-STARTPTS, scale=${leveys}x${korkeus} [lowerright]; \
            [base][upperleft] overlay=[tmp1]; \
            [tmp1][upperright] overlay=x=${leveys} [tmp2]; \
            [tmp2][lowerleft] overlay=y=${korkeus} [tmp3]; \
            [tmp3][lowerright] overlay=x=${leveys}:y=${korkeus} \
        " \
        -c:v libx264 2x2_video.mkv    
}

setup
create_single_videos
create_2x2_video



