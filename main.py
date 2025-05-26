from fastapi import FastAPI, Depends, Body
from sqlalchemy.orm import Session
from database import get_db
from schemas import UserSchema, UserOut, ProductSchema, ProductOut, CartItemSchema, OrderCreateSchema, OrderResponseSchema
from crud import user_crud, product_crud, cart_crud, order_crud
from models import Base
from database import engine
from fastapi.middleware.cors import CORSMiddleware


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://127.0.0.1:5500"] for stricter control
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# User
@app.post("/register", response_model=UserOut)
def register(user: UserSchema, db: Session = Depends(get_db)):
    return user_crud.create_user(db, user)

@app.post("/login", response_model=UserOut)
def login(user: UserSchema, db: Session = Depends(get_db)):
    db_user = user_crud.get_user(db, user.user_id)
    if db_user.password != user.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return db_user


@app.get("/users/{user_id}", response_model=UserOut)
def get_user(user_id: str, db: Session = Depends(get_db)):
    return user_crud.get_user(db, user_id)

# Product
@app.post("/products", response_model=ProductOut)
def add_product(product: ProductSchema, db: Session = Depends(get_db)):
    return product_crud.create_product(db, product)

"""@app.get("/products", response_model=list[ProductOut])
def list_products(db: Session = Depends(get_db)):
    return product_crud.get_all_products(db)

@app.get("/products/{product_id}", response_model=ProductOut)
def get_product(product_id: str, db: Session = Depends(get_db)):
    product = product_crud.get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product"""

@app.get("/products", response_model=list[ProductOut])
def list_products(db: Session = Depends(get_db)):
    return product_crud.get_all_products(db)



@app.put("/products/{product_id}", response_model=ProductOut)
def update_product(product_id: str, data: dict = Body(...), db: Session = Depends(get_db)):
    return product_crud.update_product(db, product_id, data)


@app.delete("/products/{product_id}")
def delete_product(product_id: str, db: Session = Depends(get_db)):
    return product_crud.delete_product(db, product_id)


@app.post("/cart/add")
def add_to_cart(item: CartItemSchema, db: Session = Depends(get_db)):
    return cart_crud.add_to_cart(db, item)

@app.get("/cart/{user_id}")
def view_cart(user_id: str, db: Session = Depends(get_db)):
    return cart_crud.get_cart(db, user_id)

@app.delete("/cart/{user_id}/{product_id}")
def remove_item(user_id: str, product_id: str, db: Session = Depends(get_db)):
    return cart_crud.remove_from_cart(db, user_id, product_id)

@app.post("/orders/place", response_model=OrderResponseSchema)
def place_order(order: OrderCreateSchema, db: Session = Depends(get_db)):
    return order_crud.place_order(db, order)

