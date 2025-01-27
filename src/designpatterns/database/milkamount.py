from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from designpatterns.database.base import Base
from designpatterns.database.receiptname import ReceiptName


class MilkAmount(Base):
    """Define table with milk ingredient information."""

    __tablename__ = 'milk'
    id = Column(Integer, primary_key=True)
    id_receipt = Column(Integer, ForeignKey(ReceiptName.id), unique=True)
    amount = Column(String)

    receipt = relationship('ReceiptName', uselist=False, backref='milk')
