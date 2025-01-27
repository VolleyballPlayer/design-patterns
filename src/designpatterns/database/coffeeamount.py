from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from designpatterns.database.base import Base
from designpatterns.database.receiptname import ReceiptName


class CoffeeAmount(Base):
    """Define table with coffee ingredient information."""

    __tablename__ = 'coffee'
    id = Column(Integer, primary_key=True)
    id_receipt = Column(Integer, ForeignKey(ReceiptName.id), unique=True)
    amount = Column(String, nullable=False)

    receipt = relationship('ReceiptName', uselist=False, backref='coffee')
