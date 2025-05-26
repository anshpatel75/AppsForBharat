from sqlalchemy.orm import Session
from models import Cart, Order, OrderItem
from schemas import OrderCreateSchema
from uuid import uuid4
from fastapi import HTTPException


def place_order(db: Session, order_data: OrderCreateSchema):
    cart_items = db.query(Cart).filter(Cart.user_id == order_data.user_id).all()
    if not cart_items:
        raise HTTPException(status_code=400, detail="Cart is empty")

    order_id = str(uuid4())
    new_order = Order(order_id=order_id, user_id=order_data.user_id)
    db.add(new_order)
    db.flush()

    for item in cart_items:
        db.add(OrderItem(order_id=order_id, product_id=item.product_id, quantity=item.quantity))

    db.query(Cart).filter(Cart.user_id == order_data.user_id).delete()
    db.commit()

    return new_order
