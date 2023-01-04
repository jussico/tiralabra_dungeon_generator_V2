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
    # python src/main.py $width $height video 666 dfs dijkstra silent 1000
    # python src/main.py $width $height video 666 dfs astar silent 1000
    # TODO
    # # python src/main.py $width $height video 666 dfs astar_jump_point silent 10
    # python src/main.py $(($width/10)) $(($height/10)) video 666 dfs memento_random silent 1000 # slow
    # python src/main.py $width $height video 666 dfs wall_follower silent 1000

    # create videos
    root=$(pwd)
    cd video_images/
    for hakemisto in * ; do
        echo $hakemisto
        cd "$hakemisto"/
            bash "$root/scripts/create_video.sh" "video_images/$hakemisto" "$hakemisto"
            pwd
            ls
            mv *.avi ../../videos/
            # mv *.{avi,mp4} ../../videos/
            # mv "$hakemisto"/*.{avi,mp4} ../../videos/
            # mv *.{avi,mp4} ../../videos/
        cd -
    done
    cd $root
}

function extend_video_lengths {
    pituus=$((5*60))
    cd videos/
    file1=$(ls video*-dfs_*)
    file2=$(ls video*-dfs2*)
    file3=$(ls video*-bfs_*)
    file4=$(ls video*-bfs2*)
    for file in $file1 $file2 $file3 $file4; do
        echo $file
        pituus=$(ffprobe -i $file -show_format -v quiet | sed -n 's/duration=//p' | xargs printf %.0f)
        pituus=$((10*pituus))
        ffmpeg -i $file -vf tpad=stop_mode=clone:stop_duration=$pituus extended_$file
    done
    cd -
}

function create_2x2_video {
    cd videos
    file1=$(ls extended_*-dfs_*)
    file2=$(ls extended_*-dfs2*)
    file3=$(ls extended_*-bfs_*)
    file4=$(ls extended_*-bfs2*)
    echo $file1 $file2 $file3 $file4
    leveys=$((1920/4))
    korkeus=$((1080/4))
    koko_leveys=$((1920/2))
    koko_korkeus=$((1080/2))
    echo "leveys: ${leveys} korkeus: ${korkeus}"
    ffmpeg \
        -i $file1 -i $file2 -i $file3 -i $file4 \
        -strict experimental \
        -filter_complex " \
            nullsrc=size=${koko_leveys}x${koko_korkeus} [base]; \
            [0:v] setpts=PTS-STARTPTS, scale=${leveys}x${korkeus} [upperleft]; \
            [1:v] setpts=PTS-STARTPTS, scale=${leveys}x${korkeus} [upperright]; \
            [2:v] setpts=PTS-STARTPTS, scale=${leveys}x${korkeus} [lowerleft]; \
            [3:v] setpts=PTS-STARTPTS, scale=${leveys}x${korkeus} [lowerright]; \
            [base][upperleft] overlay=shortest=1 [tmp1]; \
            [tmp1][upperright] overlay=x=${leveys}:shortest=1 [tmp2]; \
            [tmp2][lowerleft] overlay=y=${korkeus}:shortest=1 [tmp3]; \
            [tmp3][lowerright] overlay=x=${leveys}:y=${korkeus}:shortest=1 \
        " \
        -c:v libx264 \
        -preset ultrafast \
        -crf 0 2x2_video.mkv    
}

setup
create_single_videos
extend_video_lengths
create_2x2_video
