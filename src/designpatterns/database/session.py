from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, scoped_session, sessionmaker
from sqlalchemy.orm.attributes import InstrumentedAttribute
from sqlalchemy_utils import database_exists, drop_database

from designpatterns.database.base import Base
from designpatterns.database.chocolateamount import ChocolateAmount
from designpatterns.database.coffeeamount import CoffeeAmount
from designpatterns.database.milkamount import MilkAmount
from designpatterns.database.milkfoamamount import MilkFoamAmount
from designpatterns.database.receiptname import ReceiptName
from designpatterns.helpers.receipts import (
    Receipt,
    cappuccino_receipt,
    double_espresso_receipt,
    espresso_receipt,
    latte_receipt,
    triple_espresso_receipt,
)


class Session:
    """Create session manager."""

    def __init__(self, connection_string: str) -> None:
        self._engine = create_engine(connection_string)
        self._session = scoped_session(sessionmaker())
        self._session.configure(bind=self._engine, autoflush=False, expire_on_commit=False)

    def create_all(self) -> None:
        """Create all tables."""
        Base.metadata.bind = self._engine
        Base.metadata.create_all(self._engine, checkfirst=True)

    def add(self, obj: DeclarativeBase) -> None:
        """Add entry in database."""
        self._session.add(obj)
        return obj

    def add_all(self, objects: list[DeclarativeBase]) -> None:
        """Add multiple entries in database."""
        self._session.add_all(objects)

    def commit(self) -> None:
        """Commit changes to database."""
        self._session.commit()

    def empty_table(self, tablename: str) -> None:
        """Empty database table."""
        self._session.query(Base.metadata.tables[tablename]).delete()

    def query(self, obj: InstrumentedAttribute) -> None:
        """Extract data from database."""
        return self._session.query(obj)


SQLITE_DATABASE_URL = 'sqlite:///' + str(Path(Path(__file__).parent, 'receipt.db'))

if database_exists(SQLITE_DATABASE_URL):
    drop_database(SQLITE_DATABASE_URL)

session = Session(SQLITE_DATABASE_URL)
session.create_all()

for receipt in [
    latte_receipt,
    cappuccino_receipt,
    espresso_receipt,
    double_espresso_receipt,
    triple_espresso_receipt,
]:
    receipt_name = ReceiptName(name=receipt.name)
    coffee = CoffeeAmount(amount=receipt.coffee, receipt=receipt_name)
    milk = MilkAmount(amount=receipt.milk, receipt=receipt_name)
    milk_foam = MilkFoamAmount(amount=receipt.milk_foam, receipt=receipt_name)
    chocolate = ChocolateAmount(amount=receipt.chocolate, receipt=receipt_name)

    session.add_all([coffee, milk, milk_foam, chocolate])
    session.commit()

latte_receipt_db = Receipt.get_from_db(name='latte', session=session)
cappuccino_receipt_db = Receipt.get_from_db(name='cappuccino', session=session)
espresso_receipt_db = Receipt.get_from_db(name='espresso', session=session)
double_espresso_receipt_db = Receipt.get_from_db(name='double_espresso', session=session)
triple_espresso_receipt_db = Receipt.get_from_db(name='triple_espresso', session=session)
