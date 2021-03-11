from app import db
from models.base import BaseModel
from models.order_history import OrderHistory
from models.wishlist import Wishlist

class Product(db.Model, BaseModel):
    __tablename__ = "product"

    product_name = db.Column(db.String(100), nullable=False)
    product_image = db.Column(db.Text, nullable=False)
    brand = db.Column(db.Text, nullable=True)
    size = db.Column(db.String(10), nullable=False)
    description = db.Column(db.String(1000), nullable=True)
    catogory = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    condition = db.Column(db.Text, nullable=False)
    in_stock = db.Column(db.Boolean, nullable=False)
    gender = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"))


    # user = db.relationship('User', backref='product')
    wishlist = db.relationship('Wishlist', backref='product', cascade="all, delete")
    order_history = db.relationship('OrderHistory', backref='product', cascade="all, delete")
