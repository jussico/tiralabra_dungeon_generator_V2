#!/bin/bash

# create new poetry project. OVERWRITES pyproject.toml -file.
# another way try..
# poetry new --src dungv2
# mv dungv2/pyproject.toml .
# rm -rf dungv2/

# init project. skip interaction. 
# can't seem to create include-section.
poetry init --python "^3.8"  --name dungv2 -n
poetry install

# main dependencies
poetry add blessed
poetry add pipreqs
poetry add invoke

# development dependencies
poetry add pytest -G dev
poetry add coverage -G dev

echo "@end of $0"
