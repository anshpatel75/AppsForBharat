from sqlalchemy import Column, String, Integer, Boolean
from database import Base

class Product(Base):
    __tablename__ = "products"
    product_id = Column(String, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)
    inventory = Column(Integer)
    image = Column(String, nullable=True)

class User(Base):
    __tablename__ = "users"
    user_id = Column(String, primary_key=True, index=True)
    password = Column(String)
    is_admin = Column(Boolean, default=False)
