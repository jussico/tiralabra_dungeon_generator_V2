
import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from main import Main

main_class = Main()

# python src/main.py 320 256 dummy 42 dfs bfs silent 1000
main_class.main(['main.py', \
    320, 256, 'dummy', 42, 'dfs', 'bfs', 'silent', 1000])
