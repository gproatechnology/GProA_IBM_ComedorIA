# app/models/menu.py
from app import db

class Menu(db.Model):
    __tablename__ = 'menus'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    nutritional_info = db.Column(db.Text)  # Optional
    available = db.Column(db.Boolean, default=True)
    date = db.Column(db.Date, nullable=False)

    orders = db.relationship('Order', backref='menu', lazy=True)
    inventories = db.relationship('Inventory', backref='menu', lazy=True)

    def __repr__(self):
        return f'<Menu {self.name}>'