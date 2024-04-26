import os
import logging
from flask import Flask
from flask_migrate import Migrate
from src.config.database import db
from src.seed.seed import seed_data
from src.controllers import Payment, Health

migrate = Migrate()


def create_app():
    app = Flask(__name__)
    # app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:1234@mysql:3306/tax_payment_system"
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost:3306/tax_payment_system"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)
    # Seed
    # seed_data(app)
    app.register_blueprint(Payment.bp)
    app.register_blueprint(Health.bp)

    return app
