import json

from designpatterns.logger import logger


class Flyweight:
    """The Flyweight stores a common portion of the state (also called intrinsic state).

    Intrinsic state belongs to multiple real business entities. The Flyweight accepts the rest of the state
    (extrinsic state, unique for each entity) via its method parameters.
    """

    def __init__(self, shared_state: str) -> None:
        self._shared_state = shared_state

    def operation(self, unique_state: str) -> None:
        """Print intrinsic and shared state."""
        s = json.dumps(self._shared_state)
        u = json.dumps(unique_state)
        logger.info(f'Flyweight: Displaying shared ({s}) and unique ({u}) state.')


class FlyweightFactory:
    """The Flyweight Factory creates and manages the Flyweight objects.

    It ensures that flyweights are shared correctly. When the client requests a flyweight, the factory either returns
    an existing instance or creates a new one, if it doesn't exist yet.
    """

    _flyweights: dict[str, Flyweight] = {}

    def __init__(self, initial_flyweights: dict) -> None:
        for state in initial_flyweights:
            self._flyweights[self.get_key(state)] = Flyweight(state)

    def get_key(self, state: dict) -> str:
        """Return a Flyweight's string hash for a given state."""
        return '_'.join(sorted(state))

    def get_flyweight(self, shared_state: dict) -> Flyweight:
        """Return an existing Flyweight with a given state or creates a new one."""
        key = self.get_key(shared_state)

        if not self._flyweights.get(key):
            logger.info("FlyweightFactory: Can't find a flyweight, creating new one.")
            self._flyweights[key] = Flyweight(shared_state)
        else:
            logger.info('FlyweightFactory: Reusing existing flyweight.')

        return self._flyweights[key]

    def list_flyweights(self) -> None:
        """Print existing flyweights."""
        count = len(self._flyweights)
        logger.info(f'FlyweightFactory: I have {count} flyweights:')
        print('\n'.join(map(str, self._flyweights.keys())), end='')


def add_coffee_to_order_list(factory: FlyweightFactory, coffee_name: str, customer_name: str) -> None:
    """Add ordered coffee to the order list."""
    logger.info(f'Client: Adding an ordered {coffee_name} coffee.')
    flyweight = factory.get_flyweight([coffee_name])
    # The client code either stores or calculates extrinsic state and passes it
    # to the flyweight's methods.
    flyweight.operation([customer_name])
