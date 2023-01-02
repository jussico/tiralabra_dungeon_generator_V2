
# Käyttöohje

## Asennus

Poetry työkalu pitää olla asennettuna.

[python-poetry.org](https://python-poetry.org/docs/)

Riippuvuuksien asennus komennolla:

```bash
poetry install
```

## Suorittaminen

scripts/ -hakemistossa on muutama valmis Bash-scripti joilla voi ajaa ohjelmaa eri argumenteilla.

```bash
scripts/test_running_all_solving_console_visualizer.sh
scripts/test_running_all_solving_video_visualizer.sh
scripts/run_9nish_videos_and_create_high_resolution_videos.sh
```

Pääohjelma käynnistetään seuraavasti:

```python
python src/main.py <leveys> <korkeus> <visualizer> <random-generator-key> <generator-algorithm> <solving-algorithm> <silent/interactive> <framedrop>
```

esim. seuraava luo sokkelon kokoa 20x20, console-visualisoijalla, satunnais-generaattoriavaimella 42, generaattorilla dfs, ratkaisijalla dfs, hiljaisesti, näyttäen ratkaisussa joka 10. framen.
```
 python src/main.py 20 20 console 42 dfs dfs silent 10
 ```

seuraava tekee melkein saman interaktiivisesti wall_follower -algoritmilla näyttäen jokaisen framen.
```
 python src/main.py 20 20 console 43 dfs wall_follower interactive 1
 ```
