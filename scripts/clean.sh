#!/bin/bash

rm -rf build/
rm logia.txt
rm -rf .pytest_cache/
rm -rf htmlcov/

# __pycache__/ first files then folders
find . -regex '^.*\(__pycache__\|\.py[co]\)$' -delete
find . -type d -name __pycache__ -exec rm {} \;

rm .coverage
rm poetry.lock
rm -rf *.dat

# not needed anymore(?)
py3clean .
