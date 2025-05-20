from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import uuid4
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory storage
users = {}
products = {}
carts = {}
orders = {}

# Models
class User(BaseModel):
    user_id: str = Field(...)
    password: str

class Product(BaseModel):
    product_id: str
    name: str
    description: str
    price: float
    inventory: int

class CartItem(BaseModel):
    product_id: str
    quantity: int

class OrderItem(BaseModel):
    product_id: str
    quantity: int

class Order(BaseModel):
    order_id: str
    user_id: str
    items: List[OrderItem]
    status: str = "Placed"

# Helper
def get_cart(user_id: str):
    return carts.setdefault(user_id, [])

# Auth
@app.post("/register")
def register(user: User):
    if user.user_id in users:
        raise HTTPException(status_code=400, detail="User already exists")
    users[user.user_id] = user.password
    return {"message": "User registered successfully"}

@app.post("/login")
def login(user: User):
    if users.get(user.user_id) != user.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful"}

# Product APIs
@app.post("/products")
def add_product(product: Product):
    if product.product_id in products:
        raise HTTPException(status_code=400, detail="Product ID already exists")
    products[product.product_id] = product
    return {"message": "Product added"}

@app.get("/products", response_model=List[Product])
def list_products(skip: int = 0, limit: int = 10):
    return list(products.values())[skip: skip + limit]

@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: str):
    if product_id not in products:
        raise HTTPException(status_code=404, detail="Product not found")
    return products[product_id]

# Cart APIs
@app.post("/cart/add")
def add_to_cart(user_id: str, item: CartItem):
    cart = get_cart(user_id)
    cart.append(item)
    return {"message": "Item added to cart"}

@app.get("/cart")
def view_cart(user_id: str):
    return get_cart(user_id)

@app.delete("/cart/remove/{product_id}")
def remove_from_cart(user_id: str, product_id: str):
    cart = get_cart(user_id)
    carts[user_id] = [item for item in cart if item.product_id != product_id]
    return {"message": "Item removed"}

# Order APIs
@app.post("/orders/create")
def create_order(user_id: str):
    cart = get_cart(user_id)
    if not cart:
        raise HTTPException(status_code=400, detail="Cart is empty")
    order_id = str(uuid4())
    order_items = [OrderItem(product_id=item.product_id, quantity=item.quantity) for item in cart]
    order = Order(order_id=order_id, user_id=user_id, items=order_items)
    orders.setdefault(user_id, []).append(order)
    carts[user_id] = []
    return {"order_id": order_id, "status": "Placed", "payment": "Success"}

@app.get("/orders/history", response_model=List[Order])
def order_history(user_id: str, skip: int = 0, limit: int = 5):
    return orders.get(user_id, [])[skip: skip + limit]
