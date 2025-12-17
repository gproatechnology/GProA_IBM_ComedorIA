# app/blueprints/reports.py
from flask import Blueprint, request, jsonify
from flask_login import login_required
from app import db
from app.models import Order, Menu
from sqlalchemy import func
from datetime import datetime, timedelta

reports_bp = Blueprint('reports', __name__)

@reports_bp.route('/daily', methods=['GET'])
@login_required
def daily_report():
    date_str = request.args.get('date', datetime.today().strftime('%Y-%m-%d'))
    date = datetime.strptime(date_str, '%Y-%m-%d').date()

    orders = db.session.query(
        Menu.name,
        func.sum(Order.quantity).label('total_quantity')
    ).join(Order).filter(
        func.date(Order.timestamp) == date
    ).group_by(Menu.name).all()

    return jsonify([{'menu': o[0], 'quantity': o[1]} for o in orders]), 200

@reports_bp.route('/weekly', methods=['GET'])
@login_required
def weekly_report():
    start_date = datetime.today() - timedelta(days=7)
    orders = db.session.query(
        Menu.name,
        func.sum(Order.quantity).label('total_quantity')
    ).join(Order).filter(
        Order.timestamp >= start_date
    ).group_by(Menu.name).all()

    return jsonify([{'menu': o[0], 'quantity': o[1]} for o in orders]), 200

@reports_bp.route('/popular', methods=['GET'])
@login_required
def popular_menus():
    orders = db.session.query(
        Menu.name,
        func.sum(Order.quantity).label('total_quantity')
    ).join(Order).group_by(Menu.name).order_by(func.sum(Order.quantity).desc()).limit(10).all()

    return jsonify([{'menu': o[0], 'quantity': o[1]} for o in orders]), 200