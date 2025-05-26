from sqlalchemy.orm import Session
from models import Product
from schemas import ProductSchema
from fastapi import HTTPException

def create_product(db: Session, product: ProductSchema):
    if db.query(Product).filter_by(product_id=product.product_id).first():
        raise HTTPException(status_code=400, detail="Product already exists")
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_product(db: Session, product_id: str):
    product = db.query(Product).filter_by(product_id=product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

def get_all_products(db: Session):
    return db.query(Product).all()

def get_product_by_id(db: Session, product_id: str):
    return db.query(Product).filter(Product.product_id == product_id).first()



def update_product(db: Session, product_id: str, updated_data: dict):
    product = db.query(Product).filter(Product.product_id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    for key, value in updated_data.items():
        setattr(product, key, value)

    db.commit()
    db.refresh(product)
    return product


def delete_product(db: Session, product_id: str):
    product = db.query(Product).filter(Product.product_id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    db.delete(product)
    db.commit()
    return {"message": "Product deleted successfully"}

