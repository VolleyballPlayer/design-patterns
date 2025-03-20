# design-patterns

#### Project Status

[![CI](https://github.com/VolleyballPlayer/design-patterns/actions/workflows/ci.yml/badge.svg)](https://github.com/VolleyballPlayer/design-patterns/actions/workflows/ci.yml)
[![Lint](https://github.com/VolleyballPlayer/design-patterns/actions/workflows/linter.yml/badge.svg)](https://github.com/VolleyballPlayer/design-patterns/actions/workflows/linter.yml)
[![Documentation](https://github.com/VolleyballPlayer/design-patterns/actions/workflows/gh-pages.yml/badge.svg)](https://github.com/VolleyballPlayer/design-patterns/actions/workflows/gh-pages.yml)
[![Wheels](https://github.com/VolleyballPlayer/design-patterns/actions/workflows/wheels.yml/badge.svg)](https://github.com/VolleyballPlayer/design-patterns/actions/workflows/wheels.yml)
[![SDist](https://github.com/VolleyballPlayer/design-patterns/actions/workflows/sdist.yml/badge.svg)](https://github.com/VolleyballPlayer/design-patterns/actions/workflows/sdist.yml)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)

#### Documentation

Documentation can be found here: https://volleyballplayer.github.io/design-patterns/

#### About project

This project was created to document knowledge on design patterns, create examples and go back to summaries when using design patterns in other projects. This repository is work in progress also related to different topics with the goal of enriching and demonstrating the know-how related to Python packages, tests, documentation, git workflows, Docker etc.

$${\color{lightblue}Builder}$$, $${\color{lightblue}factory method}$$ and $${\color{lightblue}abstract factory}$$ patterns are used to prepare
different types of coffees: Latte, Cappuccino or Espresso.
$${\color{lightblue}Singleton}$$ pattern is counting number of prepared coffees in the builder.
$${\color{lightblue}Prototype}$$ pattern is creating prototype for double espresso coffee using existing espresso coffee class.

$${\color{lightblue}Adapter}$$ pattern is providing same interface for printing in tabular form for 2 different classes.
$${\color{lightblue}Facade}$$ pattern is creating one interface for two command design patterns.
$${\color{lightblue}Brigde}$$ pattern implements separates coffee class from specific coffee types classes and enables easy extension
for futures types and combinations.
$${\color{lightblue}Composite}$$ pattern implements menu with prices structuring drinks by size and type.
$${\color{lightblue}Flyweight}$$ pattern reuses existing coffee type and adds customer name to new order.
$${\color{lightblue}Decorator}$$ pattern adds decorators for notifications and payments around the coffee order.
$${\color{lightblue}Proxy}$$ pattern keeps track of prepared coffees in the cache. In case the coffee was already prepared, provide to coffee to customer, else prepare the coffee.

$${\color{lightblue}Strategy}$$ pattern is preparing coffees using same method for
different ways of preparations per coffee type.
$${\color{lightblue}Observer}$$ pattern is informing subscribed customer about workday or weekend discounts.
$${\color{lightblue}Command}$$ pattern is executing steps like receiving order, preparing coffee etc.
$${\color{lightblue}Mediator}$$ pattern is establishing independent order, preparation and payment classes and providing them with notifications about state of each.
$${\color{lightblue}Template method}$$ pattern provides full process around ordering latte and cappuccino by reusing steps that
are common for each order with specifying them in the base class. Specific steps concerning each coffee receipt are implemented in subclasses.
$${\color{lightblue}Iterator}$$ pattern iterates over increasing or decreasing coffee prices in the menu.
$${\color{lightblue}Chain of responsibility}$$ pattern takes an ingredient and adds it to first corresponding product which requires it.
$${\color{lightblue}Visitor}$$ pattern extracts different data from recipes.
$${\color{lightblue}State}$$ pattern check if certain coffee type was already prepared and should be sent to payment or it should be firstly made.

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

https://medium.com/@amirm.lavasani/design-patterns-in-python-factory-method-1882d9a06cb4

https://medium.com/@amirm.lavasani/design-patterns-in-python-adapter-58eb7cc11474

https://medium.com/@amirm.lavasani/design-patterns-in-python-mediator-ca42c2caca52

##### UML
https://www.visual-paradigm.com/guide/uml-unified-modeling-language/uml-class-diagram-tutorial/

https://plantuml.com/class-diagram

https://stackoverflow.com/questions/27660499/open-arrow-with-solid-line-in-uml
