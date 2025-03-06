from __future__ import annotations

from abc import ABC, abstractmethod

from designpatterns.logger import logger


class Handler(ABC):
    """The Handler interface declares a method for building the chain of handlers.

    It also declares a method for executing a request.
    """

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        """Set next handler."""

    @abstractmethod
    def handle(self, request: str) -> str:
        """Define method that will be applied in the chain."""


class AbstractHandler(Handler):
    """The default chaining behavior can be implemented inside a base handler class."""

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        """Set next handler."""
        self._next_handler = handler
        # Returning a handler from here will let us link handlers in a convenient way like this:
        # handler1 -> set_next(handler2) ->  set_next(handler3)
        return handler

    @abstractmethod
    def handle(self, request: str) -> str:
        """Define method that will be applied in the chain."""
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


"""Concrete Handlers either handle a request or pass it to the next handler in the chain."""


class CoffeeHandler(AbstractHandler):
    """Concrete handler."""

    def handle(self, request: str) -> str:
        """Define method that will be applied in the chain."""
        if request in ['water', 'sugar']:
            return f'Coffee gets {request}'
        return super().handle(request)


class CakeHandler(AbstractHandler):
    """Concrete handler."""

    def handle(self, request: str) -> str:
        """Define method that will be applied in the chain."""
        if request in ['sugar']:
            return f'Cake gets {request}'
        return super().handle(request)


class TeaHandler(AbstractHandler):
    """Concrete handler."""

    def handle(self, request: str) -> str:
        """Define method that will be applied in the chain."""
        if request in ['honey', 'water']:
            return f'Tea gets {request}'
        return super().handle(request)


def client_code(handler: Handler) -> None:
    """Work with a single handler usually.

    In most cases, it is not even aware that the handler is part of a chain.
    """
    for ingredient in ['honey', 'water', 'sugar']:
        logger.info(f'\nCLient: I have some {ingredient}. Which product should i start making with it?')
        result = handler.handle(ingredient)
        if result:
            logger.info(result)
        else:
            logger.info(f'{ingredient} was left unused. There is no product that needs it.')
