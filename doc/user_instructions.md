
# Käyttöohje

## Asennus

Poetry työkalu pitää olla asennettuna.

[python-poetry.org](https://python-poetry.org/docs/)

Riippuvuuksien asennus komennolla:

```bash
poetry install
```

## Status

Projektissa on tällä hetkellä kolme hieman erilaista
algoritmien toiminnan visualisoijaa. ( src/visualizer/ )

Yksikkötestit ja suorituskykytestit eivät vielä tee mitään 
vaikka rungot niiden käytölle on luotu.

Sokkelonluontialgoritmeista on toteutettu vasta ensimmäinen - 
Randomized DFS.

Polunetsintäalgoritmeja ei ole vielä toteutettu.

## Suorittaminen

scripts/ -hakemistossa on muutama valmis Bash-scripti joilla voi ajaa ohjelman toimivia osia (DFS-generointialgoritmi kolmella eri visualisointitavalla).

```bash
scripts/suorita_ascii_visualizer.sh
scripts/suorita_mini_console_visualizer.sh
scripts/suorita_console_visualizer.sh
```

Pääohjelma käynnistetään seuraavasti:

```python
python src/main.py <leveys> <korkeus> <visualizer>
```

esim.

```python
python src/main.py 20 20 ascii

python src/main.py 20 20 consolemini

python src/main.py 20 20 console
```
