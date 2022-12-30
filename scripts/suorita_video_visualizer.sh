#!/bin/bash

# python src/main.py 20 20 video
# python src/main.py 160 128 video
# python src/main.py 320 256 video

# ok
# python src/main.py 900 500 video -1 dfs dfs


python src/main.py $((640/2)) $((512/2)) dummy 46 dfs dfs

