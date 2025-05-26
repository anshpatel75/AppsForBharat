from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import Base
#from app.models import Base


class User(Base):
    __tablename__ = "users"
    user_id = Column(String, primary_key=True)
    password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)

class Product(Base):
    __tablename__ = "products"
    product_id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Integer, nullable=False)
    inventory = Column(Integer, nullable=False)
    image = Column(String, nullable=False)

"""class Order(Base):
    __tablename__ = "orders"
    order_id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.user_id"))
    status = Column(String)"""

class Cart(Base):
    __tablename__ = "carts"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, nullable=False)
    product_id = Column(String, ForeignKey("products.product_id"), nullable=False)
    quantity = Column(Integer, default=1)

    product = relationship("Product")


class Order(Base):
    __tablename__ = "orders"
    order_id = Column(String, primary_key=True, index=True)
    user_id = Column(String, nullable=False)
    status = Column(String, default="Placed")


class OrderItem(Base):
    __tablename__ = "order_items"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(String, ForeignKey("orders.order_id"))
    product_id = Column(String, ForeignKey("products.product_id"))
    quantity = Column(Integer)

    product = relationship("Product")
