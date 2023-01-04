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

function create_images_for_videos {
    width=$((1920/6))
    height=$((1080/6))
    echo "width: $width height: $height"
    # run algorithms
    python src/main.py $width $height video 666 dfs dfs silent 100
    python src/main.py $width $height video 666 dfs bfs silent 100
    python src/main.py $width $height video 666 dfs dfs_randomized silent 100
    python src/main.py $width $height video 666 dfs bfs_randomized silent 100
    python src/main.py $width $height video 666 dfs dijkstra silent 100
    python src/main.py $width $height video 666 dfs astar silent 100
    # TODO
    # python src/main.py $width $height video 666 dfs astar_jump_point silent 10
    # python src/main.py $(($width/10)) $(($height/10)) video 666 dfs memento_random silent 1000 # slow
    # python src/main.py $width $height video 666 dfs memento_random silent 1000000 # too slow
    python src/main.py $((width/3)) $((height/3)) video 666 dfs memento_random silent 100000 # ?
    python src/main.py $width $height video 666 dfs wall_follower silent 100
}

function create_single_videos {
    # create videos
    root=$(pwd)
    cd video_images/
    for hakemisto in * ; do
        echo $hakemisto
        cd "$hakemisto"/
            bash "$root/scripts/create_video.sh" "video_images/$hakemisto" "$hakemisto"
            mv *.avi ../../videos/
        cd -
    done
    cd $root
}

function extend_video_lengths {
    cd videos/
    file1=$(ls video*-dfs_*)
    file2=$(ls video*-bfs_*)
    file3=$(ls video*-dfs2*)
    file4=$(ls video*-bfs2*)
    file5=$(ls video*-dijkstra*)
    file6=$(ls video*-astar*)
    file7=$(ls video*-memento_random*)
    file8=$(ls video*-wall_follower*)
    max=0
    for file in $file1 $file2 $file3 $file4 $file5 $file6 $file7 $file8; do
        pituus=$(ffprobe -i $file -show_format -v quiet | sed -n 's/duration=//p' | xargs printf %.0f)
        echo "testaillaan! pituus: ${pituus} max: ${max}"
        if (( max < pituus )); then
            max=$pituus
        fi
    done
    echo "max: ${max}"
    for file in $file1 $file2 $file3 $file4 $file5 $file6 $file7 $file8; do
        echo $file
        pituus=$(( 2*max ))
        echo $pituus
        ffmpeg -i $file -vf tpad=stop_mode=clone:stop_duration=$pituus extended_$file
    done
    cd -
}

function create_3x3_video {
    cd videos
    file1=$(ls extended_*-dfs_*)
    file2=$(ls extended_*-bfs_*)
    file3=$(ls extended_*-dfs2*)
    file4=$(ls extended_*-bfs2*)
    file5=$(ls extended_*-dijkstra*)
    file6=$(ls extended_*-astar*)
    file7=$(ls extended_*-memento_random*)
    file8=$(ls extended_*-wall_follower*)
    
    # TODO: change to astar_jump_point
    file9=$(ls extended_*-wall_follower*)

    echo $file1 $file2 $file3 $file4 $file5 $file6 $file7 $file8 $file9
    leveys=$((1920/6))
    korkeus=$((1080/6))
    koko_leveys=$((1920/2))
    koko_korkeus=$((1080/2))
    echo "leveys: ${leveys} korkeus: ${korkeus}"
    ffmpeg \
        -i $file1 -i $file2 -i $file3 -i $file4 -i $file5 -i $file6 -i $file7 -i $file8 -i $file9 \
        -strict experimental \
        -filter_complex " \
            nullsrc=size=${koko_leveys}x${koko_korkeus} [base]; \
            [0:v] setpts=PTS-STARTPTS, scale=${leveys}x${korkeus} [upperleft]; \
            [1:v] setpts=PTS-STARTPTS, scale=${leveys}x${korkeus} [uppermiddle]; \
            [2:v] setpts=PTS-STARTPTS, scale=${leveys}x${korkeus} [upperright]; \
            [3:v] setpts=PTS-STARTPTS, scale=${leveys}x${korkeus} [middleleft]; \
            [4:v] setpts=PTS-STARTPTS, scale=${leveys}x${korkeus} [middle]; \
            [5:v] setpts=PTS-STARTPTS, scale=${leveys}x${korkeus} [middleright]; \
            [6:v] setpts=PTS-STARTPTS, scale=${leveys}x${korkeus} [lowerleft]; \
            [7:v] setpts=PTS-STARTPTS, scale=${leveys}x${korkeus} [lowermiddle]; \
            [8:v] setpts=PTS-STARTPTS, scale=${leveys}x${korkeus} [lowerright]; \
            [base][upperleft] overlay=shortest=1 [tmp1]; \
            [tmp1][uppermiddle] overlay=x=${leveys}:shortest=1 [tmp2]; \
            [tmp2][upperright] overlay=x=$((2*leveys)):shortest=1 [tmp3]; \
            [tmp3][middleleft] overlay=y=${korkeus}:shortest=1 [tmp4]; \
            [tmp4][middle] overlay=x=${leveys}:y=${korkeus}:shortest=1 [tmp5]; \
            [tmp5][middleright] overlay=x=$((2*leveys)):y=${korkeus}:shortest=1 [tmp6]; \
            [tmp6][lowerleft] overlay=y=$((2*korkeus)):shortest=1 [tmp7]; \
            [tmp7][lowermiddle] overlay=x=${leveys}:y=$((2*korkeus)):shortest=1 [tmp8]; \
            [tmp8][lowerright] overlay=x=$((2*leveys)):y=$((2*korkeus)):shortest=1 \
        " \
        -c:v libx264 \
        -preset ultrafast \
        -crf 0 3x3_video.mkv    
}

setup
create_images_for_videos
create_single_videos
extend_video_lengths
create_3x3_video
