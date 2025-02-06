from designpatterns.database.session import session
from designpatterns.helpers.receipts import Receipt, latte_receipt


class TestReceipts:
    def test__get_from_db__same_ingredients_as_in_receipt_class(self) -> None:
        latte_receipt_db = Receipt.get_from_db(name='latte', session=session)
        assert latte_receipt_db.name == latte_receipt.name
        assert latte_receipt_db.coffee == latte_receipt.coffee
        assert latte_receipt_db.milk == latte_receipt.milk
        assert latte_receipt_db.milk_foam == latte_receipt.milk_foam
        assert latte_receipt_db.chocolate == latte_receipt.chocolate
