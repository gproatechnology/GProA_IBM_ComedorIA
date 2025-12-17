# app/blueprints/orders.py
from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from app import db
from app.models import Order, Menu, Inventory
from datetime import datetime

orders_bp = Blueprint('orders', __name__)

@orders_bp.route('/', methods=['GET'])
@login_required
def get_orders():
    orders = Order.query.filter_by(user_id=current_user.id).all()
    return jsonify([{
        'id': o.id,
        'menu_name': o.menu.name,
        'quantity': o.quantity,
        'timestamp': o.timestamp.isoformat()
    } for o in orders]), 200

@orders_bp.route('/', methods=['POST'])
@login_required
def create_order():
    data = request.get_json()
    menu_id = data['menu_id']
    quantity = data.get('quantity', 1)

    menu = Menu.query.get_or_404(menu_id)
    if not menu.available:
        return jsonify({'message': 'Menu not available'}), 400

    # Check inventory
    inventory = Inventory.query.filter_by(menu_id=menu_id, date=datetime.today().date()).first()
    if inventory and inventory.available_quantity < quantity:
        return jsonify({'message': 'Insufficient inventory'}), 400

    order = Order(user_id=current_user.id, menu_id=menu_id, quantity=quantity)
    db.session.add(order)
    if inventory:
        inventory.available_quantity -= quantity
    db.session.commit()
    return jsonify({'message': 'Order created', 'id': order.id}), 201

@orders_bp.route('/<int:id>', methods=['DELETE'])
@login_required
def cancel_order(id):
    order = Order.query.filter_by(id=id, user_id=current_user.id).first_or_404()
    # Restore inventory
    inventory = Inventory.query.filter_by(menu_id=order.menu_id, date=datetime.today().date()).first()
    if inventory:
        inventory.available_quantity += order.quantity
    db.session.delete(order)
    db.session.commit()
    return jsonify({'message': 'Order cancelled'}), 200