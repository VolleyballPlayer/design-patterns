from collections import Counter

import pytest

from designpatterns.behavioral_patterns.iterator import PriceCollection


class TestIterator:
    def test__run_iterator__get_output(self, capsys: pytest.CaptureFixture[str]) -> None:
        collection = PriceCollection()
        collection.add_item('Espresso: €1')
        collection.add_item('Double Espresso: €2')
        collection.add_item('Triple Espresso: €3')
        collection.add_item('Cappuccino: €4')
        collection.add_item('Latte: €5')

        print('\n'.join(collection))
        print('\n')
        print('\n'.join(collection.get_reverse_iterator()), end='')

        captured = capsys.readouterr()
        captured_split = captured.out.split('\n')
        count = Counter(captured_split)
        assert count['Espresso: €1'] == 2
        assert count['Double Espresso: €2'] == 2
        assert count['Triple Espresso: €3'] == 2
        assert count['Cappuccino: €4'] == 2
        assert count['Latte: €5'] == 2
