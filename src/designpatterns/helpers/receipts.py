from __future__ import annotations

from dataclasses import dataclass

from designpatterns.logger import logger


@dataclass
class Receipt:
    """Set coffee drink contents."""

    name: str
    coffee: str
    milk: str = None
    milk_foam: str = None
    chocolate: str = None

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
    name='double_espresso', coffee='3 shots coffee', milk=None, milk_foam=None, chocolate=None
)
