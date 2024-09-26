from dataclasses import dataclass


@dataclass
class Receipt:
    """Set coffee drink contents."""

    coffee: str
    milk: str
    milk_foam: str
    chocolate: str


latte_receipt = Receipt(
    coffee='1/2 cup coffee', milk='1/4 cup milk', milk_foam='1/4 cup milk foam', chocolate='No chocolate'
)

cappuccino_receipt = Receipt(
    coffee='1/2 cup coffee', milk='1/6 cup milk', milk_foam='1/6 cup milk foam', chocolate='1/6 cup chocolate'
)

espresso_receipt = Receipt(coffee='1 cup coffee', milk='No milk', milk_foam='No milk foam', chocolate='No chocolate')
