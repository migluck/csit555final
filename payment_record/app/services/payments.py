from app.config.database import db
from app.models.Payment import Payment
from flask import abort

def create_payment(data):
    Payment = Payment(**data)
    db.session.add(payment)
    db.session.commit()
    return payment.to_dict()  # Assume you implement a to_dict method in your Payment model

def get_all_payment():
    payments = Payment.query.all()
    if not payments:
        abort(404)
    return payments
