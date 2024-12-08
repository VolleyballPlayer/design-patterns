from dataclasses import dataclass


@dataclass
class Receipt:
    """Set coffee drink contents."""

    name: str
    coffee: str
    milk: str
    milk_foam: str
    chocolate: str


latte_receipt = Receipt(
    name='latte', coffee='1/2 cup coffee', milk='1/4 cup milk', milk_foam='1/4 cup milk foam', chocolate='no chocolate'
)

cappuccino_receipt = Receipt(
    name='cappuccino',
    coffee='1/2 cup coffee',
    milk='1/6 cup milk',
    milk_foam='1/6 cup milk foam',
    chocolate='1/6 cup chocolate',
)

espresso_receipt = Receipt(
    name='espresso', coffee='1 shot coffee', milk='no milk', milk_foam='no milk foam', chocolate='no chocolate'
)

double_espresso_receipt = Receipt(
    name='double_espresso', coffee='2 shots coffee', milk='no milk', milk_foam='no milk foam', chocolate='no chocolate'
)

triple_espresso_receipt = Receipt(
    name='double_espresso', coffee='3 shots coffee', milk='no milk', milk_foam='no milk foam', chocolate='no chocolate'
)
