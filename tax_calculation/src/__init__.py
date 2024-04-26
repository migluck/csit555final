from flask import Flask
from src.controllers import Tax, Health

def create_app():
    app = Flask(__name__)
    # Controller blueprints
    app.register_blueprint(Tax.bp)
    app.register_blueprint(Health.bp)

    return app
