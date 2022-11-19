# Testausdokumentti

## Yksikkötestaus

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


## Suorituskyvin testaus

Omassa dokumentissaan:
[Suorituskyky testaus](test_performance_document.md)