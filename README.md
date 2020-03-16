
## CLI (no docker)

(env)$ export FLASK_APP=project/__init__.py
(env)$ export FLASK_ENV=development
(env)$ python manage.py run


$ docker-compose build

$ docker-compose up -d
Update container
$ docker-compose up -d --build

Pytest

### normal run
$ docker-compose exec users pytest "project/tests"

### disable warnings
$ docker-compose exec users pytest "project/tests" -p no:warnings

### run only the last failed tests
$ docker-compose exec users pytest "project/tests" --lf

### run only the tests with names that match the string expression
$ docker-compose exec users pytest "project/tests" -k "config and not test_development_config"

### stop the test session after the first failure
$ docker-compose exec users pytest "project/tests" -x

### enter PDB after first failure then end the test session
$ docker-compose exec users pytest "project/tests" -x --pdb

### stop the test run after two failures
$ docker-compose exec users pytest "project/tests" --maxfail=2

### show local variables in tracebacks
$ docker-compose exec users pytest "project/tests" -l

### list the 2 slowest tests
$ docker-compose exec users pytest "project/tests"  --durations=2