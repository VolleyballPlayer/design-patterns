import pytest

from designpatterns.behavioral_patterns.visitor import (
    CappuccinoComponent,
    CoffeeVisitor,
    LatteComponent,
    MilkVisitor,
    client_code,
)


class TestVisitor:
    def test__run_visitor__get_output(self, caplog: pytest.LogCaptureFixture) -> None:
        components = [LatteComponent(), CappuccinoComponent()]
        coffee_visitor = CoffeeVisitor()
        client_code(components, coffee_visitor)
        milk_visitor = MilkVisitor()
        client_code(components, milk_visitor)
        for log_message in [
            'Latte contains 1/2 cup coffee',
            'Cappuccino contains 1/2 cup coffee',
            'Latte contains 1/4 cup milk',
            'Cappuccino contains 1/6 cup milk',
        ]:
            assert log_message in caplog.text
