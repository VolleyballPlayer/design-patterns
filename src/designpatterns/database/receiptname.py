from sqlalchemy import Column, Integer, String

from designpatterns.database.base import Base


class ReceiptName(Base):
    """Define table with receipt name information."""

    __tablename__ = 'receipt'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
