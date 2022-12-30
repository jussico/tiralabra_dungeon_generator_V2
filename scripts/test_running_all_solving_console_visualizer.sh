#!/bin/bash

set -e

silent="silent"
# key=666
key=42
# silent="interactive"
python src/main.py 25 25 console $key dfs dfs $silent 10
python src/main.py 25 25 console $key dfs bfs $silent 10
python src/main.py 25 25 console $key dfs dfs_randomized $silent 10
python src/main.py 25 25 console $key dfs bfs_randomized $silent 10
python src/main.py 25 25 console $key dfs dijkstra $silent 10
python src/main.py 25 25 console $key dfs astar $silent 10
# TODO
# python src/main.py 25 25 console $key dfs astar_jump_point $silent 10
python src/main.py 25 25 console $key dfs memento_random $silent 1000 # slow
python src/main.py 25 25 console $key dfs wall_follower $silent 10
