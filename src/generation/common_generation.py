from enum import Enum

class Generation(Enum):
  dummy = 0
  dfs = 1
  bfs = 2

# testing
if __name__ == '__main__':
  pass
  print(Generation._member_names_)