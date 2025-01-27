from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from designpatterns.database.base import Base
from designpatterns.database.receiptname import ReceiptName


class ChocolateAmount(Base):
    """Define table with chocolate ingredient information."""

    __tablename__ = 'chocolate'
    id = Column(Integer, primary_key=True)
    id_receipt = Column(Integer, ForeignKey(ReceiptName.id), unique=True)
    amount = Column(String)

    receipt = relationship('ReceiptName', uselist=False, backref='chocolate')
