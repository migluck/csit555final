from src.models.Payment import Payment
from src.config.database import db


data = [
    {'company': 'derm', 'amount': 4100.00, 'payment_date': '09/26/2023', 'status': 'paid', 'due_date': '01/15/2024'},
    {'company': 'derm', 'amount': 4100.00, 'payment_date': '10/12/2023', 'status': 'paid', 'due_date': '01/15/2024'},
    {'company': 'tek', 'amount': 15200.00, 'payment_date': '06/09/2023', 'status': 'paid', 'due_date': '06/15/2023'},
    {'company': 'tek', 'amount': 15200.00, 'payment_date': '07/12/2023', 'status': 'paid', 'due_date': '09/15/2023'},
    {'company': 'tek', 'amount': 11400.00, 'payment_date': '08/11/2023', 'status': 'paid', 'due_date': '09/15/2023'},
    {'company': 'tek', 'amount': 14440.00, 'payment_date': '09/21/2023', 'status': 'paid', 'due_date': '01/15/2024'},
    {'company': 'tek', 'amount': 15200.00, 'payment_date': '10/18/2023', 'status': 'paid', 'due_date': '01/15/2024'},
    {'company': 'tek', 'amount': 23520.00, 'status': 'unpaid', 'due_date': '01/15/2024'},
    {'company': 'tek', 'amount': 16800.00, 'status': 'unpaid', 'due_date': '01/15/2024'},
    {'company': 'tek', 'amount': 16800.00, 'status': 'unpaid', 'due_date': '01/15/2024'},
    {'company': 'tek', 'amount': 16800.00, 'status': 'unpaid', 'due_date': '01/15/2024'}
]




def seed_data(app):
    with app.app_context():
        try:
                # Delete existing data
                db.session.query(Payment).delete()
                # Add new data
                for item in data:
                    payment = Payment(**item)
                    db.session.add(payment)
                db.session.commit()
                print("Data inserted successfully.")
        except Exception as e:
            db.session.rollback()
            print(f"An error occurred: {e}")
