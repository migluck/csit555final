import logging

from src.config.database import db
from src.models.Payment import Payment
from flask import abort

def create_payment(data):
    Payment = Payment(**data)
    db.session.add(payment)
    db.session.commit()
    return payment.to_dict()  # Assume you implement a to_dict method in your Payment model

def get_all_payment():
    payments = Payment.query.all()
    logging.info(f"Hereare: {{payments}}")
    if not payments:
        abort(404)
    return payments
