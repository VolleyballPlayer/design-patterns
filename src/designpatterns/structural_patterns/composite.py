from __future__ import annotations

from abc import ABC, abstractmethod


class Component(ABC):
    """The base Component class declares common operations for both simple and complex objects of a composition."""

    @property
    def parent(self) -> Component:
        """Parent getter."""
        return self._parent

    @parent.setter
    def parent(self, parent: Component) -> Component:
        """Optionally, the base Component can declare an interface for setting and accessing a parent of the component.

        It can also provide some default implementation for these methods.
        """
        self._parent = parent

    """
    In some cases, it would be beneficial to define the child-management operations right in the base Component class.
    This way, you won't need to expose any concrete component classes to the client code, even during the object tree
    assembly. The downside is that these methods will be empty for the leaf-level components.
    """

    def add(self, component: Component) -> None:  # noqa: B027
        """Add component."""

    def remove(self, component: Component) -> None:  # noqa: B027
        """Remove component."""

    def is_composite(self) -> bool:
        """You can provide a method that lets the client code figure out whether a component can bear children."""
        return False

    @abstractmethod
    def operation(self) -> str:
        """Implement some default behavior or leave it to concrete classes.

        It does it by declaring the method containing the behavior as "abstract").
        """


class Leaf(Component):
    """The Leaf class represents the end objects of a composition. A leaf can't have any children.

    Usually, it's the Leaf objects that do the actual work, whereas Composite objects only delegate to their
    sub-components.
    """

    def __init__(self, type_: str) -> None:
        self._type = type_

    def operation(self) -> str:
        """Implement behavior."""
        return self._type


class Composite(Component):
    """The Composite class represents the complex components that may have children.

    Usually, the Composite objects delegate the actual work to their children and then "sum-up" the result.
    """

    def __init__(self, type_: str) -> None:
        self._children: list[Component] = []
        self._type = type_

    """
    A composite object can add or remove other components (both simple orcomplex) to or from its child list.
    """

    def add(self, component: Component) -> None:
        """Add children components."""
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        """Remove children components."""
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        """Check whether a component can bear children."""
        return True

    def operation(self) -> str:
        """Execute its primary logic in a particular way.

        It traverses recursively through all its children, collecting and summing their results. Since the composite's
        children pass these calls to their children and so forth, the whole object tree is traversed as a result.
        """
        results = []
        for child in self._children:
            results.append(child.operation())
        joined_results = '\n'.join(results)
        return f'{self._type}\n{joined_results}'


def client_code(component: Component) -> None:
    """Works with all of the components via the base interface."""
    print(f'RESULT: {component.operation()}', end='')


def client_code2(component1: Component, component2: Component) -> None:
    """Work with any component, simple or complex.

    ...thanks to the fact that the child-management operations are declared in the base Component class,
    without depending on their concrete classes.
    """
    if component1.is_composite():
        component1.add(component2)

    print(f'RESULT: {component1.operation()}', end='')
