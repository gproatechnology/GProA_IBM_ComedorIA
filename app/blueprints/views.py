# app/blueprints/views.py
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user

views_bp = Blueprint('views', __name__)

@views_bp.route('/')
def index():
    return render_template('index.html')

@views_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login via JS
        pass
    return render_template('login.html')

@views_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@views_bp.route('/kiosk')
def kiosk():
    return render_template('kiosk.html')

@views_bp.route('/admin')
@login_required
def admin():
    if current_user.role != 'admin':
        return redirect(url_for('views.dashboard'))
    return render_template('admin.html')