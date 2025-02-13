import pytest

from designpatterns.behavioral_patterns.strategy import Context, StrategyCappuccino, StrategyEspresso, StrategyLatte
from designpatterns.helpers.receipts import Receipt, cappuccino_receipt, latte_receipt


class TestStrategy:
    def test__run_strategy__get_latte(self, capsys: pytest.CaptureFixture[str]) -> None:
        context = Context(StrategyLatte())
        context.prepare_coffee()
        captured = capsys.readouterr()
        assert latte_receipt.name in captured.out
        assert latte_receipt.coffee in captured.out
        assert latte_receipt.milk in captured.out
        assert latte_receipt.milk_foam in captured.out

    def test__run_strategy__get_cappuccino(self, caplog: pytest.LogCaptureFixture) -> None:
        context = Context(StrategyCappuccino())
        context.prepare_coffee()
        assert (
            f'Your {cappuccino_receipt.name} will be prepared using following ingredients: \n\
{cappuccino_receipt.coffee}\n{cappuccino_receipt.milk}\n{cappuccino_receipt.milk_foam}\n{cappuccino_receipt.chocolate}'
            in caplog.text
        )

    def test__run_strategy__get_espresso(self, caplog: pytest.LogCaptureFixture) -> None:
        context = Context(StrategyEspresso())
        context.prepare_coffee()
        assert Receipt.get_coffee(receipt=latte_receipt) in caplog.text

    def test__setter__set_strategy_subclass(self) -> None:
        context = Context(StrategyLatte())
        context.prepare_coffee()
        context.strategy = StrategyCappuccino()
        assert isinstance(context.strategy, StrategyCappuccino) is True

    def test__getter__get_strategy_subclass(self) -> None:
        context = Context(StrategyLatte())
        assert isinstance(context.strategy, StrategyLatte) is True
