from flask import Flask
from flask_migrate import Migrate
from app.config.database import db
from app.controllers import Payment

import os
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost/academic_records"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(Payment.bp)

    return app
