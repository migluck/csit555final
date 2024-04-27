import logging
from datetime import datetime
from src.config.database import db
from src.models.Payment import Payment
from flask import abort


def get_all_payments():
    payments = Payment.query.all()
    if not payments:
        abort(404)
    return [payment.to_dict() for payment in payments]


def get_payment_by_id(payment_id):
    return Payment.query.get(payment_id)

def create_payment(data):
    new_payment = Payment(
        company=data['company'],
        amount=data['amount'],
        payment_date=data['payment_date'],
        status=data['status'],
        due_date=data['due_date']
    )
    db.session.add(new_payment)
    db.session.commit()
    return new_payment

def update_payment(payment_id, data):
    payment = get_payment_by_id(payment_id)
    if payment:
        payment.company = data.get('company', payment.company)
        payment.amount = data.get('amount', payment.amount)
        payment.status = data.get('status', payment.status)
        payment.payment_date = datetime.strptime(data['payment_date'], '%m/%d/%Y') if data.get('payment_date') else payment.payment_date
        payment.due_date = datetime.strptime(data['due_date'], '%m/%d/%Y') if data.get('due_date') else payment.due_date
        db.session.commit()
    return payment

def delete_payment(payment_id):
    payment = get_payment_by_id(payment_id)
    if payment:
        db.session.delete(payment)
        db.session.commit()
        return True
    return False
