import click

from designpatterns.behavioral_patterns.chain_of_responsibility import (
    CakeHandler,
    CoffeeHandler,
    TeaHandler,
    client_code as client_code_chain_of_responsibility,
)
from designpatterns.behavioral_patterns.command import Invoker, OrderCommand, PrepareCoffeeCommand, Receiver
from designpatterns.behavioral_patterns.iterator import PriceCollection
from designpatterns.behavioral_patterns.mediator import Coffee, ConcreteMediator, Order, Payment
from designpatterns.behavioral_patterns.memento import Caretaker, Originator
from designpatterns.behavioral_patterns.observer import (
    DiscountPublisher,
    ObserverWeekendDiscounts,
    ObserverWorkDayDiscounts,
)
from designpatterns.behavioral_patterns.state import (
    Context as ContextState,
    Latte as LatteState,
)
from designpatterns.behavioral_patterns.strategy import (
    Context,
    StrategyCappuccino,
    StrategyEspresso,
    StrategyLatte,
)
from designpatterns.behavioral_patterns.template_method import (
    Cappuccino,
    Latte,
    client_code as client_code_template_method,
)
from designpatterns.behavioral_patterns.visitor import (
    CappuccinoComponent,
    CoffeeVisitor,
    LatteComponent,
    MilkVisitor,
    client_code as client_code_visitor,
)
from designpatterns.helpers.receipts import latte_receipt
from designpatterns.logger import logger
from designpatterns.utilities.package_resources import PackageResources


@click.group()
def cli() -> None:
    """Run behavioral patterns."""
    logger.info(f'Using design patterns package version {PackageResources.get_package_version()}')


@cli.command()
def strategy() -> None:
    """Run strategy example.

    This function calls strategy module to run an example of behavioral design pattern called strategy.
    """
    logger.info('Starting strategy pattern run')

    context = Context(StrategyLatte())
    context.prepare_coffee()

    context.strategy = StrategyCappuccino()
    context.prepare_coffee()

    context.strategy = StrategyEspresso()
    context.prepare_coffee()


@cli.command()
def observer() -> None:
    """Run observer example.

    This function calls observer module to run an example of behavioral design pattern called observer.
    """
    logger.info('Starting observer pattern run')

    subject = DiscountPublisher()

    observer_a = ObserverWorkDayDiscounts()
    subject.attach(observer_a)
    observer_b = ObserverWorkDayDiscounts()
    subject.attach(observer_b)

    observer_c = ObserverWeekendDiscounts()
    subject.attach(observer_c)

    subject.send_discounts()

    subject.detach(observer_a)

    subject.send_discounts()


@cli.command()
def command() -> None:
    """Run command example.

    This function calls command module to run an example of behavioral design pattern called command.
    """
    logger.info('Starting command pattern run')

    invoker = Invoker()
    invoker.set_on_start(OrderCommand(latte_receipt))
    receiver = Receiver()
    invoker.set_on_finish(PrepareCoffeeCommand(receiver, latte_receipt, 'John Smith'))
    invoker.execute_commands_in_order()


@cli.command()
def mediator() -> None:
    """Run mediator example.

    This function calls mediator module to run an example of behavioral design pattern called mediator.
    """
    logger.info('Starting mediator pattern run')

    mediator = ConcreteMediator()

    order = Order(mediator)
    coffee = Coffee(mediator)
    payment = Payment(mediator)

    mediator.add_component(order)
    mediator.add_component(coffee)
    mediator.add_component(payment)

    order.process(coffee=latte_receipt.name)
    coffee.prepare(coffee=latte_receipt.name)
    payment.receive(coffee=latte_receipt.name)


@cli.command()
def template_method() -> None:
    """Run template method example.

    This function calls template_method module to run an example of behavioral design pattern called template method.
    """
    logger.info('Starting template method pattern run')

    client_code_template_method(Latte())
    client_code_template_method(Cappuccino())


@cli.command()
def iterator() -> None:
    """Run iterator method example.

    This function calls iterator module to run an example of behavioral design pattern called iterator.
    """
    logger.info('Starting iterator pattern run')

    # The client code may or may not know about the Concrete Iterator or Collection classes, depending on the level of
    # indirection you want to keep in your program.

    collection = PriceCollection()
    collection.add_item('Espresso: €1')
    collection.add_item('Double Espresso: €2')
    collection.add_item('Triple Espresso: €3')
    collection.add_item('Cappuccino: €4')
    collection.add_item('Latte: €5')

    logger.info('Increasing price order:')
    print('\n'.join(collection))
    print('\n')

    logger.info('Decreasing price order:')
    print('\n'.join(collection.get_reverse_iterator()), end='')


@cli.command()
def chain_of_responsibility() -> None:
    """Run chain of responsibility method example.

    This function calls chain of responsibility module to run an example of behavioral design pattern called
    chain of responsibility.
    """
    logger.info('Starting chain of responsibility pattern run')

    coffee = CoffeeHandler()
    cake = CakeHandler()
    tea = TeaHandler()

    coffee.set_next(cake).set_next(tea)

    # The client should be able to send a request to any handler, not just the first one in the chain.

    logger.info('Chain: Coffee > Cake > Tea')
    client_code_chain_of_responsibility(coffee)
    print('\n')
    logger.info('Subchain: Tea')
    client_code_chain_of_responsibility(tea)


@cli.command()
def visitor() -> None:
    """Run visitor method example.

    This function calls visitor module to run an example of behavioral design pattern called visitor.
    """
    logger.info('Starting visitor pattern run')

    components = [LatteComponent(), CappuccinoComponent()]
    logger.info('The client code works with all visitors via the base Visitor interface:')
    coffee_visitor = CoffeeVisitor()
    client_code_visitor(components, coffee_visitor)
    logger.info('It allows the same client code to work with different types of visitors:')
    milk_visitor = MilkVisitor()
    client_code_visitor(components, milk_visitor)


@cli.command()
def state() -> None:
    """Run state method example.

    This function calls state module to run an example of behavioral design pattern called state.
    """
    logger.info('Starting state pattern run')

    context = ContextState(LatteState())
    context.check_order(coffee='latte')
    context.process_order()

    context.check_order(coffee='cappuccino')
    context.process_order()


@cli.command()
def memento() -> None:
    """Run memento method example.

    This function calls memento module to run an example of behavioral design pattern called memento.
    """
    logger.info('Starting memento pattern run')

    originator = Originator('espresso')
    caretaker = Caretaker(originator)
    caretaker.backup()
    originator.receive_order('latte')

    caretaker.backup()
    originator.receive_order('cappuccino')

    caretaker.backup()
    originator.receive_order('latte')

    caretaker.show_history()

    logger.info("Client: Now, let's rollback!")
    caretaker.undo()

    logger.info('Client: Once more!')
    caretaker.undo()

    logger.info('Client: Once more!')
    caretaker.undo()


if __name__ == '__main__':
    cli()
