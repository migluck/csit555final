from flask import Flask
from src.controllers import Reporting, Health

def create_app():
    app = Flask(__name__)
    # Controller blueprints
    app.register_blueprint(Reporting.bp)
    app.register_blueprint(Health.bp)

    return app
