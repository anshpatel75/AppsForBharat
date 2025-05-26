from sqlalchemy.orm import Session
from models import Cart
from schemas import CartItemSchema


def add_to_cart(db: Session, item: CartItemSchema):
    cart_item = db.query(Cart).filter(
        Cart.user_id == item.user_id, Cart.product_id == item.product_id
    ).first()

    if cart_item:
        cart_item.quantity += item.quantity
    else:
        cart_item = Cart(**item.dict())
        db.add(cart_item)

    db.commit()
    db.refresh(cart_item)
    return cart_item


def get_cart(db: Session, user_id: str):
    return db.query(Cart).filter(Cart.user_id == user_id).all()


def remove_from_cart(db: Session, user_id: str, product_id: str):
    db.query(Cart).filter(Cart.user_id == user_id, Cart.product_id == product_id).delete()
    db.commit()
    return {"message": "Removed"}
