import pytest

from designpatterns.behavioral_patterns.memento import Caretaker, Originator


class TestMemento:
    def test__run_memento__get_output(self, caplog: pytest.LogCaptureFixture) -> None:
        originator = Originator('espresso')
        caretaker = Caretaker(originator)
        caretaker.backup()
        originator.receive_order('latte')
        caretaker.show_history()
        caretaker.undo()
        caretaker.undo()

        for text in [
            'Originator: My initial state is: espresso',
            "Caretaker: Saving Originator's state...",
            "Originator: I'm checking the next order.",
            'Received an order for latte coffee drink',
            'Originator: and my state has changed to: latte',
            'Caretaker: Restoring state to',
        ]:
            assert text in caplog.text
