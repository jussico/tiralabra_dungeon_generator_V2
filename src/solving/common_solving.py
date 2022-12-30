from enum import Enum

class Solving(Enum):
  dfs = 1
  bfs = 2
  dfs_randomized = 3
  bfs_randomized = 4
  dijkstra = 5
  astar = 6
  astar_jump_point = 7 # TODO
  memento_random = 8
  wall_follower = 9

# testing

if __name__ == '__main__':
    pass
    # print(Solving._member_names_)
