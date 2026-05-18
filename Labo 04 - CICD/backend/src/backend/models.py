from sqlalchemy import Column, Double, Integer, String

from .database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String, index=True)
    price = Column(Double, index=True, nullable=False)