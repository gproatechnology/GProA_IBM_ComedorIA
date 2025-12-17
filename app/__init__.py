# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
from .config import Config

db = SQLAlchemy()
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    from .models import User
    return User.query.get(int(user_id))

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    with app.app_context():
        db.create_all()

    from .blueprints.auth import auth_bp
    from .blueprints.menu import menu_bp
    from .blueprints.orders import orders_bp
    from .blueprints.reports import reports_bp
    from .blueprints.views import views_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(menu_bp, url_prefix='/api/menu')
    app.register_blueprint(orders_bp, url_prefix='/api/orders')
    app.register_blueprint(reports_bp, url_prefix='/api/reports')
    app.register_blueprint(views_bp)

    return app