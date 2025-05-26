from pydantic import BaseModel
from typing import List

DATABASE_URL = "postgresql://storeuser:storepass@localhost/mobilestore"



class UserSchema(BaseModel):
    user_id: str
    password: str
    is_admin: bool = False

class UserOut(BaseModel):
    user_id: str
    is_admin: bool
    class Config:
        orm_mode = True

class ProductSchema(BaseModel):
    product_id: str
    name: str
    description: str
    price: int
    inventory: int
    image: str

class ProductOut(ProductSchema):
    class Config:
        orm_mode = True



class CartItemSchema(BaseModel):
    user_id: str
    product_id: str
    quantity: int


class OrderItemSchema(BaseModel):
    product_id: str
    quantity: int


class OrderCreateSchema(BaseModel):
    user_id: str


class OrderResponseSchema(BaseModel):
    order_id: str
    user_id: str
    status: str

    class Config:
        orm_mode = True
