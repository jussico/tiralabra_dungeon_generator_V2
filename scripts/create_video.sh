#!/bin/bash

cd $1

filename="$2"

# ffmpeg -framerate 25 -i frame_%07d.pbm -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p video.mp4

# latest
# ffmpeg -framerate 60 -i frame_%07d.pbm -c:v libx264rgb -crf 0 video.mp4

#ffmpeg -framerate 10 -i image%05d.png -c:v libx264rgb -crf 0 output.mp4

# mpv video.mp4

# ffmpeg -framerate 60 -i frame_%07d.pbm -c:v libx264rgb -crf 0 "$filename".mp4

# ffmpeg -framerate 60 -i frame_%07d.pbm -c:v libx264rgb -vcodec aac -strict -2 "$filename".mp4

# ffmpeg -framerate 60 -i frame_%07d.pbm -c:v libx264rgb -strict -2 "$filename".mp4
# ffmpeg -framerate 60 -i frame_%07d.pbm -c:v libx264 -strict -2 "$filename".mp4
# ffmpeg -framerate 60 -i frame_%07d.pbm -libcodec libx264 -vcodec aac -strict -2 "$filename".mp4

# ffmpeg -f image2 -r 60 -i frame_%07d.pbm -vcodec libx264 -profile:v high444 -refs 16 -crf 0 -preset ultrafast a.mp4
# ffmpeg -f image2 -r 60 -i frame_%07d.pbm -vcodec libx264 -profile:v high444 -refs 32 -crf 0 "$filename".mp4
# ffmpeg -f image2 -r 60 -i frame_%07d.pbm -vcodec libx265 -x265-params lossless=1 -refs 32 -crf 0 "$filename".mp4

ffmpeg -r 60 -f image2 -i frame_%07d.pbm -vcodec png "$filename".avi
