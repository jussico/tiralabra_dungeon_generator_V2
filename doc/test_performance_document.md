# Suorituskyky testausdokumentti

## Suorituskyvin testauksessa on käytetty kahta yleiskäyttöistä työkalua:
* /usr/bin/time
* python memory profiler

https://man7.org/linux/man-pages/man1/time.1.html

https://pypi.org/project/memory-profiler/

### Suorituskyvin testausscriptit ovat hakemistossa performance_test/

``` bash
install_dependencies.sh
run_tests.sh
```

### Testien ajaminen

Suorituskykytestien ajaminen tapahtuu komennolla ```bash performance_test/run_tests.sh```

Tämä ajaa scriptissä määritellyt python-tiedostot sekä python 
memory profilerilla että ```/usr/bin/time``` -komennolla.

Tulokset kopioidaan doc/resources/ -hakemistoon.

## Suorituskykytestien tulokset

### /usr/bin/time

tulokset:
doc/resource/ tiedostot

#### Python Memory Profiler

tulokset alla:

![alt text](resource/mp_report_astar_default.png)
![alt text](resource/mp_report_astar_flame.png)
![alt text](resource/mp_report_astar_slope.png)
![alt text](resource/mp_report_bfs_default.png)
![alt text](resource/mp_report_bfs_flame.png)
![alt text](resource/mp_report_bfs_randomized_default.png)
![alt text](resource/mp_report_bfs_randomized_flame.png)
![alt text](resource/mp_report_bfs_randomized_slope.png)
![alt text](resource/mp_report_bfs_slope.png)
![alt text](resource/mp_report_dfs_default.png)
![alt text](resource/mp_report_dfs_flame.png)
![alt text](resource/mp_report_dfs_randomized_default.png)
![alt text](resource/mp_report_dfs_randomized_flame.png)
![alt text](resource/mp_report_dfs_randomized_slope.png)
![alt text](resource/mp_report_dfs_slope.png)
![alt text](resource/mp_report_dijkstra_default.png)
![alt text](resource/mp_report_dijkstra_flame.png)
![alt text](resource/mp_report_dijkstra_slope.png)
![alt text](resource/mp_report_memento_random_default.png)
![alt text](resource/mp_report_memento_random_flame.png)
![alt text](resource/mp_report_memento_random_slope.png)
![alt text](resource/mp_report_wall_follower_default.png)
![alt text](resource/mp_report_wall_follower_flame.png)
![alt text](resource/mp_report_wall_follower_slope.png)
