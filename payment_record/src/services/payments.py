import logging
from datetime import datetime
from src.config.database import db
from src.models.Payment import Payment
from flask import abort

def create_payment(data):
    payment = Payment(
        company=data.get('company'),
        amount=data.get('amount'),
        payment_date=datetime.strptime(data.get('payment_date'), '%Y/%m/%d').date() if data.get('payment_date') else None,
        status=data.get('status'),
        due_date=datetime.strptime(data.get('due_date'), '%Y/%m/%d').date() if data.get('due_date') else None
    )
    db.session.add(payment)
    db.session.commit()
    return payment

def get_all_payment():
    payments = Payment.query.all()
    logging.debug("Data to be returned: %s", payments)
    if not payments:
        abort(404)
    return [payment.to_dict() for payment in payments]
