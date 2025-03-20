import pytest

from designpatterns.behavioral_patterns.state import Cappuccino, Context, Latte


class TestState:
    def test__run_state_starting_with_latte__get_output(self, caplog: pytest.LogCaptureFixture) -> None:
        context = Context(Latte())
        context.check_order(coffee='latte')
        context.process_order()

        context.check_order(coffee='cappuccino')
        context.process_order()

        for text in [
            'Context: Transition to Latte',
            'Order was made for latte.',
            'Preparing latte.',
            'Order was not made for latte. Check if it was made for cappuccino.',
            'Context: Transition to Cappuccino',
            'Preparing cappuccino',
        ]:
            assert text in caplog.text

    def test__run_state_starting_with_cappuccino__get_output(self, caplog: pytest.LogCaptureFixture) -> None:
        context = Context(Cappuccino())
        context.check_order(coffee='cappuccino')
        context.process_order()

        context.check_order(coffee='latte')
        context.process_order()

        for text in [
            'Context: Transition to Cappuccino',
            'Order was made for cappuccino.',
            'Preparing cappuccino',
            'Order was not made for cappuccino. Check if it was made for latte.',
            'Context: Transition to Latte',
            'Preparing latte',
        ]:
            assert text in caplog.text
