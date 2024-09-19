# design-patterns

#### Project Status

[![CI](https://github.com/VolleyballPlayer/design-patterns/actions/workflows/ci.yml/badge.svg)](https://github.com/VolleyballPlayer/design-patterns/actions/workflows/ci.yml)
[![Lint](https://github.com/VolleyballPlayer/design-patterns/actions/workflows/linters.yml/badge.svg)](https://github.com/VolleyballPlayer/design-patterns/actions/workflows/linters.yml)
[![gh-pages](https://github.com/VolleyballPlayer/design-patterns/actions/workflows/gh-pages.yml/badge.svg)](https://github.com/VolleyballPlayer/design-patterns/actions/workflows/gh-pages.yml)

#### Documentation

Documentation can be found here: https://volleyballplayer.github.io/design-patterns/

#### About project

This project was created to document knowledge on design patterns, create examples and go back to summaries when using design patterns in other projects. This repository is work in progress also related to different topics with the goal of enriching and demonstrating the know-how related to Python packages, tests, documentation, git workflows, Docker etc.

#### Installation

When creating virtual environment by Visual Studio Code and tasks.json, it is assumed that local Python version can be found under /usr/bin/python3.11. Else, one can replace this path.

##### Install with developer dependencies

``` shell
pip install -e .[dev]
```

Project can be lint via

``` shell
pylint designpatterns
```

``` shell
ruff check
ruff format
```

Additionally, Pylance can be installed as VS Code extension.

#### Tests

##### Install required dependencies for testing

``` shell
pip install -e .[test]
```

Once dependencies are installed, you can run the tests from the package root folder via

``` shell
pytest
```

Conventionally, the name of the test script should be defined by adding *test_* prefix to script name it is testing. The name of the test itself should also start with *test_* prefix such that test can be identified. Each test script starts with a class whose name starts with *Test*. Test names follow convention: *test_StateUnderTest_ExpectedBehaviour* e.g. *test_IsPackageBuilt_True()*

#### Build documentation

``` shell
pip install -e .[docs]
```

#### See also

Explanations taken from https://refactoring.guru/design-patterns/
