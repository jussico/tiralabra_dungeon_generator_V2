# Testausdokumentti

## Suorituskyvin testaus

Omassa dokumentissaan:
[Suorituskyky testaus](test_performance_document.md)

## Yksikkötestaus

Koodin looginen toimivuus testataan yksikkötestauksella. 

Testataan ohjelmaa ajamalla algoritmeja generoitujen ja kovakoodattujen sokkeloiden kanssa ja varmistetaan algoritmin toimivuus.

Käytetty kirjastoja:

Unittest:
[unittest](https://docs.python.org/3/library/unittest.html)

Coverage:
[coverage](https://coverage.readthedocs.io/en/6.5.0/)

### Testien ajaminen

#### unit-testien ajaminen
```bash
poetry run pytest
```

#### unit-testien ajaminen coveragella
```bash
poetry run coverage run --branch -m pytest
```

#### coverage-raportin luominen html
```bash
poetry run coverage html
```

#### coverage-raportin luominen html
```bash
poetry run coverage xml
```

#### Testien tulokset

##### coverage html raportti
[coverage HTML report](resource/htmlcov/index.html)

##### coverage xml raportti
[coverage XML report](resource/coverage.xml)

##### coverage html raportti kuva
![](resource/coverage_table.png?raw=true)

#### Testien kuvaus algoritmeittain

Jokainen algoritmi palauttaa parin (True/False, None/List).

Jokaisella algoritmille on oma yksikkötesti-luokkansa src/tests/solving/ hakemistossa.

Kaikille algoritmeille luodaan yhteen testiin satunnainen 32x16 sokkelo joka on muodostettu Depth First Search algoritmilla.

Neljään testiin käytetään neljää erilaista tyhjää sokkeloa joissa alkupiste sijaitsee aina koordinaateissa 0,0 ja 
loppupisteet eri kulmissa ja keskellä.

Viimeiseksi käytetään sokkeloa jossa loppupiste on saavuttamattomisas keskellä seinien ympäröimänä. Kaikilla algoritmeilla testataan että tässä sokkelossa algoritmi palauttaa onnistuneesti False.

##### A* algoritmi

```astar_test.py```

Satunnaisessa sokkelossa testataan että loppupiste löytyy ja algoritmi palauttaa jonkin listan.

Tyhjissä sokkeloissa testataan että löydetty reitti on lyhin mahdollinen.

##### Depth First Search algoritmi

```dfs_test.py```

Satunnaisessa sokkelossa testataan että loppupiste löytyy ja algoritmi palauttaa jonkin listan.

Tyhjissä sokkeloissa testataan että löydetty reitti ei ole tyhjä.

##### Randomized Depth First Search algoritmi

```dfs_randomized_test.py```

Tämä menee samoin kuin edellinen.

##### Breadth First Search algoritmi

```bfs_test.py```

Satunnaisessa sokkelossa testataan että loppupiste löytyy ja algoritmi palauttaa jonkin listan.

Tyhjissä sokkeloissa testataan että löydetty reitti on lyhin mahdollinen.

##### Randomized Breadth First Search algoritmi

```bfs_randomized_test.py```

##### Dijkstran algoritmi

```dijkstra_test.py```

Satunnaisessa sokkelossa testataan että loppupiste löytyy ja algoritmi palauttaa jonkin listan.

Tyhjissä sokkeloissa testataan että löydetty reitti on lyhin mahdollinen.

##### Memento random algoritmi

```memento_random_test.py```

Tämä algoritmi ei palauta reittiä.

Satunnaisessa sokkelossa testataan että loppupiste löytyy.

Tyhjissä sokkeloissa testataan myös että loppupiste löytyy.

##### Wall follower algoritmi

```wall_follower_test.py```

Tämä algoritmi ei palauta reittiä.

Satunnaisessa sokkelossa testataan että loppupiste löytyy.

Kolmessa tyhjässä sokkelossa joissa loppupiste on kulmassa testataan että loppupiste löytyy.

Tyhjässä sokkelossa jossa loppupiste on keskellä testataan että tämä algoritmi palauttaa onnistuneesti False.
