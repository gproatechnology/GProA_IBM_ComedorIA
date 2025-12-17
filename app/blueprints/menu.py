# app/blueprints/menu.py
from flask import Blueprint, request, jsonify
from flask_login import login_required
from app import db
from app.models import Menu
from datetime import datetime

menu_bp = Blueprint('menu', __name__)

@menu_bp.route('/', methods=['GET'])
@login_required
def get_menus():
    date_str = request.args.get('date')
    if date_str:
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        menus = Menu.query.filter_by(date=date, available=True).all()
    else:
        menus = Menu.query.filter_by(available=True).all()
    return jsonify([{
        'id': m.id,
        'name': m.name,
        'description': m.description,
        'price': m.price,
        'nutritional_info': m.nutritional_info
    } for m in menus]), 200

@menu_bp.route('/', methods=['POST'])
@login_required
def create_menu():
    data = request.get_json()
    menu = Menu(
        name=data['name'],
        description=data.get('description'),
        price=data['price'],
        nutritional_info=data.get('nutritional_info'),
        date=datetime.strptime(data['date'], '%Y-%m-%d').date()
    )
    db.session.add(menu)
    db.session.commit()
    return jsonify({'message': 'Menu created', 'id': menu.id}), 201

@menu_bp.route('/<int:id>', methods=['PUT'])
@login_required
def update_menu(id):
    menu = Menu.query.get_or_404(id)
    data = request.get_json()
    menu.name = data.get('name', menu.name)
    menu.description = data.get('description', menu.description)
    menu.price = data.get('price', menu.price)
    menu.nutritional_info = data.get('nutritional_info', menu.nutritional_info)
    menu.available = data.get('available', menu.available)
    db.session.commit()
    return jsonify({'message': 'Menu updated'}), 200

@menu_bp.route('/<int:id>', methods=['DELETE'])
@login_required
def delete_menu(id):
    menu = Menu.query.get_or_404(id)
    menu.available = False
    db.session.commit()
    return jsonify({'message': 'Menu deactivated'}), 200