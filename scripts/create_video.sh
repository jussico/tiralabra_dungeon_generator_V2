#!/bin/bash

cd $1

filename="$2"

# ffmpeg -framerate 25 -i frame_%07d.pbm -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p video.mp4

# latest
# ffmpeg -framerate 60 -i frame_%07d.pbm -c:v libx264rgb -crf 0 video.mp4

#ffmpeg -framerate 10 -i image%05d.png -c:v libx264rgb -crf 0 output.mp4

# mpv video.mp4

ffmpeg -framerate 60 -i frame_%07d.pbm -c:v libx264rgb -crf 0 "$filename".mp4

