from __future__ import annotations

from dataclasses import dataclass

from sqlalchemy.engine.base import Engine

from designpatterns.database.chocolateamount import ChocolateAmount
from designpatterns.database.coffeeamount import CoffeeAmount
from designpatterns.database.milkamount import MilkAmount
from designpatterns.database.milkfoamamount import MilkFoamAmount
from designpatterns.database.receiptname import ReceiptName
from designpatterns.logger import logger


@dataclass
class Receipt:
    """Set coffee drink contents."""

    name: str
    coffee: str
    milk: str = None
    milk_foam: str = None
    chocolate: str = None

    @classmethod
    def get_from_db(cls: type[Receipt], name: str, session: Engine) -> dict:
        """Create Receipt instance from database entries."""
        id = session.query(ReceiptName.id).filter(ReceiptName.name == name).one()[0]

        cls.name = name
        cls.coffee = session.query(CoffeeAmount.amount).filter(CoffeeAmount.id == id).one()[0]
        cls.milk = session.query(MilkAmount.amount).filter(MilkAmount.id == id).one()[0]
        cls.milk_foam = session.query(MilkFoamAmount.amount).filter(MilkFoamAmount.id == id).one()[0]
        cls.chocolate = session.query(ChocolateAmount.amount).filter(ChocolateAmount.id == id).one()[0]

        return cls

    def get_ingredients(self) -> list[str]:
        """Get all data class fields but name with a value different than None."""
        fields = []
        for field in self.__dataclass_fields__:
            value = getattr(self, field)
            if field != 'name' and value is not None:
                fields.append(value)
        return fields

    @staticmethod
    def get_coffee(receipt: Receipt, ingredients: list[str] = None) -> str:
        """Get which coffee is made with which ingredients."""
        if ingredients is None:
            ingredients = receipt.get_ingredients()
        ingredients = [ingredient for ingredient in ingredients if ingredient is not None]
        joined_ingredients = '\n'.join(ingredients)
        msg = f'Your {receipt.name} is made of: \n{joined_ingredients}.'
        logger.info(msg)
        return joined_ingredients

    def __eq__(self, other: Receipt) -> bool:
        """Define equal method."""
        if not isinstance(other, Receipt):
            return False
        return (self.name, self.coffee, self.milk, self.milk_foam, self.chocolate) == (
            other.name,
            other.coffee,
            other.milk,
            other.milk_foam,
            other.chocolate,
        )

    def __hash__(self) -> Receipt:
        """Provide hashing for Receipt class."""
        return hash((self.name, self.coffee, self.milk, self.milk_foam, self.chocolate))


latte_receipt = Receipt(
    name='latte', coffee='1/2 cup coffee', milk='1/4 cup milk', milk_foam='1/4 cup milk foam', chocolate=None
)

cappuccino_receipt = Receipt(
    name='cappuccino',
    coffee='1/2 cup coffee',
    milk='1/6 cup milk',
    milk_foam='1/6 cup milk foam',
    chocolate='1/6 cup chocolate',
)

espresso_receipt = Receipt(name='espresso', coffee='1 shot coffee', milk=None, milk_foam=None, chocolate=None)

double_espresso_receipt = Receipt(
    name='double_espresso', coffee='2 shots coffee', milk=None, milk_foam=None, chocolate=None
)

triple_espresso_receipt = Receipt(
    name='triple_espresso', coffee='3 shots coffee', milk=None, milk_foam=None, chocolate=None
)
