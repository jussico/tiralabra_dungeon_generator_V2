#!/bin/bash

set -e

python src/main.py 320 256 video 666 dfs dfs silent 1000
python src/main.py 320 256 video 666 dfs bfs silent 1000
python src/main.py 320 256 video 666 dfs dfs_randomized silent 1000
python src/main.py 320 256 video 666 dfs bfs_randomized silent 1000
python src/main.py 320 256 video 666 dfs dijkstra silent 1000
python src/main.py 320 256 video 666 dfs astar silent 1000

# TODO
# python src/main.py 320 256 video 666 dfs astar_jump_point silent 10

python src/main.py 32 25 video 666 dfs memento_random silent 1000 # slow
python src/main.py 320 256 video 666 dfs wall_follower silent 1000
