#!/bin/bash

python src/main.py 25 25 consolemini 666 dfs dfs silent
python src/main.py 25 25 consolemini 666 dfs bfs silent
python src/main.py 25 25 consolemini 666 dfs dfs_randomized silent
python src/main.py 25 25 consolemini 666 dfs bfs_randomized silent
python src/main.py 25 25 consolemini 666 dfs dijkstra silent
python src/main.py 25 25 consolemini 666 dfs astar silent

# TODO
# python src/main.py 25 25 consolemini 666 dfs astar_jump_point silent

python src/main.py 25 25 consolemini 666 dfs memento_random silent
python src/main.py 25 25 consolemini 666 dfs wall_follower silent
exit 0
