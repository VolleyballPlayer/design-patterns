import pytest

from designpatterns.creational_patterns.builder import Director
from designpatterns.creational_patterns.prototype import DoubleEspressoBuilderPrototype
from designpatterns.helpers.receipts import Receipt, double_espresso_receipt


class TestPrototype:
    def test__run_prototype__get_logs_per_number(self, caplog: pytest.LogCaptureFixture) -> None:
        director = Director()
        clone = DoubleEspressoBuilderPrototype().clone()
        director.builder = clone
        director.build_espresso()
        clone.cup.list_contents()
        assert '4. coffee is being prepared' in caplog.text
        assert Receipt.get_coffee(receipt=double_espresso_receipt) in caplog.text
