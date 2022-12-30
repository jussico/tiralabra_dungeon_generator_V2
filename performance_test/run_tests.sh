#!/bin/bash

set -ex

# https://man7.org/linux/man-pages/man1/time.1.html
# https://pypi.org/project/memory-profiler/

mkdir -p build

declare -A commands
commands=(
    ['dfs']='src/tests_performance/performance_test_dfs.py'    
    ['bfs']='src/tests_performance/performance_test_bfs.py'    
    ['dfs_randomized']='src/tests_performance/performance_test_dfs_randomized.py'    
    ['bfs_randomized']='src/tests_performance/performance_test_bfs_randomized.py'    
    ['dijkstra']='src/tests_performance/performance_test_dijkstra.py'    
    ['astar']='src/tests_performance/performance_test_astar.py'    
    ['memento_random']='src/tests_performance/performance_test_memento_random.py'    
    ['wall_follower']='src/tests_performance/performance_test_wall_follower.py'    
)

# mprof run -M python <script> --script-arg

# for name in "${executables[@]}" # values

# run python profiler on commands
echo "run python profiler on commands."
for name in "${!commands[@]}" # keys
do
    echo "name:${name}"
    command="${commands[$name]}"
    echo "command:${command}"
    dat_filename="build/mprofile_${name}_$(date +%s).dat"
    echo "dat_filename: ${dat_filename}"
    mprof run --output $dat_filename --python "$command" 
    mprof plot --title "$name default settings ($command)" --output "build/mp_report_${name}_default.png" "$dat_filename"
    mprof plot --title "$name flame settings ($command)" --output "build/mp_report_${name}_flame.png" "$dat_filename"
    mprof plot --title "$name slope settings ($command)" --output "build/mp_report_${name}_slope.png" "$dat_filename"
done

# run /usr/bin/time on commands
echo "run /usr/bin/time on commands."
for name in "${!commands[@]}" # keys
do
    echo "name:${name}"
    command="${commands[$name]}"
    echo "command:${command}"
    time_filename="time_${name}_$(date +%s).txt"
    /usr/bin/time --output=build/${time_filename} -v python "${command}"
done

mv build/*.{png,txt} doc/resource/

echo "@end."