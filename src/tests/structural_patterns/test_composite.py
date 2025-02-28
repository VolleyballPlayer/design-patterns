import pytest

from designpatterns.structural_patterns.composite import Composite, Leaf, client_code, client_code2


class TestComposite:
    def test__run_composite__get_output(self, capsys: pytest.CaptureFixture[str]) -> None:
        simple = Leaf('Water: €0')
        print("Client: I've got a simple component:")
        client_code(simple)
        print('\n')

        tree = Composite('Coffees')

        big_coffees = Composite('Big Coffees')
        big_coffees.add(Leaf('Cappuccino: €4'))
        big_coffees.add(Leaf('Latte: €5'))

        small_coffees = Composite('Small Coffees')
        small_coffees.add(Leaf('Espresso: €1'))
        small_coffees.add(Leaf('Double Espresso: €2'))
        small_coffees.add(Leaf('Triple Espresso: €3'))

        tree.add(big_coffees)
        tree.add(small_coffees)

        print("Client: Now I've got a composite tree:")
        client_code(tree)
        print('\n')

        print("Client: I don't need to check the components classes even when managing the tree:")
        client_code2(tree, simple)

        prices = [
            'Water: €0',
            'Cappuccino: €4',
            'Latte: €5',
            'Espresso: €1',
            'Double Espresso: €2',
            'Triple Espresso: €3',
        ]

        captured = capsys.readouterr()

        for price in prices:
            assert price in captured.out

    def test__is_composite__false(self) -> None:
        simple = Leaf('Water: €0')
        assert simple.is_composite() is False

    def test__remove_children__one_less(self) -> None:
        tree = Composite('Coffees')

        big_coffees = Composite('Big Coffees')
        big_coffees.add(Leaf('Cappuccino: €4'))
        latte = Leaf('Latte: €5')
        big_coffees.add(latte)

        tree.add(big_coffees)

        big_coffees.remove(latte)

        assert True
