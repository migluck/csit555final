from app import app, db
from models import Payment

try:
    with app.app_context():
        db.create_all()
        print("Tables created successfully.")
except Exception as e:
    print(f"Error creating tables: {e}")

