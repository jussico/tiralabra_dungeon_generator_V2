
# run unit-tests
echo "@test"
poetry run pytest

# run coverage
echo "@coverage"
poetry run coverage run --branch -m pytest

# # create coverage-report
echo "@coverage-report"
poetry run coverage html

cp htmlcov/*.{js,html,png,json,css} doc/resources/
