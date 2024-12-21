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

    def get_coffee(self, ingredients: list[str] = None) -> str:
        """Get which coffee is made with which ingredients."""
        if ingredients is None:
            ingredients = self.get_ingredients()
        msg = f"Your {self.name} is made of {', '.join(ingredients)}."
        logger.info(msg)
        return msg


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
