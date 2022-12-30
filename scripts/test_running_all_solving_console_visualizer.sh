#!/bin/bash

set -e

# silent="silent"
# key=666
key=42
silent="interactive"
framedrop=10
python src/main.py 25 25 console $key dfs dfs $silent $framedrop
python src/main.py 25 25 console $key dfs bfs $silent $framedrop
python src/main.py 25 25 console $key dfs dfs_randomized $silent $framedrop
python src/main.py 25 25 console $key dfs bfs_randomized $silent $framedrop
python src/main.py 25 25 console $key dfs dijkstra $silent $framedrop
python src/main.py 25 25 console $key dfs astar $silent $framedrop
# TODO
# python src/main.py 25 25 console $key dfs astar_jump_point $silent $framedrop
python src/main.py 25 25 console $key dfs memento_random $silent $((framedrop*100)) # slow
python src/main.py 25 25 console $key dfs wall_follower $silent $framedrop
