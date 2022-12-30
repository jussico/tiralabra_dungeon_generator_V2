
import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from main import Main

main_class = Main()

# python src/main.py 25 25 dummy 42 dfs dfs silent 10'    
main_class.main(['main.py', \
    25, 25, 'dummy', 42, 'dfs', 'dfs', 'silent', 1000])
