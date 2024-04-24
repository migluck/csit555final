import logging

from src.config.database import db
from src.models.Payment import Payment
from flask import abort

def create_payment(data):
    payment = Payment(**data)
    db.session.add(payment)
    db.session.commit()
    return payment.to_dict()  # Assume you implement a to_dict method in your Payment model

def get_all_payment():
    payments = Payment.query.all()
    logging.debug("Data to be returned: %s", payments)
    if not payments:
        abort(404)
    return [payment.to_dict() for payment in payments]
