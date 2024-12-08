# design-patterns

#### Project Status

[![CI](https://github.com/VolleyballPlayer/design-patterns/actions/workflows/ci.yml/badge.svg)](https://github.com/VolleyballPlayer/design-patterns/actions/workflows/ci.yml)
[![Lint](https://github.com/VolleyballPlayer/design-patterns/actions/workflows/linter.yml/badge.svg)](https://github.com/VolleyballPlayer/design-patterns/actions/workflows/linter.yml)
[![Documentation](https://github.com/VolleyballPlayer/design-patterns/actions/workflows/gh-pages.yml/badge.svg)](https://github.com/VolleyballPlayer/design-patterns/actions/workflows/gh-pages.yml)
[![Wheels](https://github.com/VolleyballPlayer/design-patterns/actions/workflows/wheels.yml/badge.svg)](https://github.com/VolleyballPlayer/design-patterns/actions/workflows/wheels.yml)

#### Documentation

Documentation can be found here: https://volleyballplayer.github.io/design-patterns/

#### About project

This project was created to document knowledge on design patterns, create examples and go back to summaries when using design patterns in other projects. This repository is work in progress also related to different topics with the goal of enriching and demonstrating the know-how related to Python packages, tests, documentation, git workflows, Docker etc.

<span style="color:lightblue">Builder pattern</span> is used to prepare different types of coffees: Latte, Cappuccino or Espresso.
<span style="color:lightblue">Singleton pattern</span> is counting number of prepared coffees and is applied in the builder, too.

#### Installation

When creating virtual environment by Visual Studio Code and tasks.json, it is assumed that local Python version can be found under /usr/bin/python3. Else, one can replace this path.

##### Install with developer dependencies

``` shell
pip install -e .[dev]
```

Project can be lint via

``` shell
ruff check
ruff format
```

#### Tests

##### Install required dependencies for testing

``` shell
pip install -e .[test]
```

Once dependencies are installed, you can run the tests from the package root folder via

``` shell
pytest
```

Conventionally, the name of the test script should be defined by adding *test_* prefix to script name it is testing. The name of the test itself should also start with *test_* prefix such that test can be identified. Each test script starts with a class whose name starts with *Test*. Test names follow convention: *test__state_under_test__expected_behaviour* e.g. *test__is_package_built__true()*

#### Build documentation

``` shell
pip install -e .[docs]
```

#### Or install with Docker

``` shell
docker build -t volleyballplayer/design-patterns:1.0 . --progress=plain --no-cache
docker run -it --name design-patterns volleyballplayer/design-patterns:1.0
```
Container has already installed design-patterns package. Source virtual environment to run CLIs.

#### Software versioning

Ubuntu approach is being used. Version numbers are defined as the year and the month of the release (YY.M).

#### See also

Explanations taken from https://refactoring.guru/design-patterns/

##### UML
https://www.visual-paradigm.com/guide/uml-unified-modeling-language/uml-class-diagram-tutorial/
https://plantuml.com/class-diagram
