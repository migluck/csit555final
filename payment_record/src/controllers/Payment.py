from flask import Blueprint, request, redirect, url_for, jsonify, render_template
from src.services  import payments
import logging
import datetime
from flask_cors import cross_origin
bp = Blueprint('payment', __name__, url_prefix='/payments')

# Get all payments
@bp.route('/', methods=['GET'])
def index():
    logging.info("Fetching all payments")
    try:
        data = payments.get_all_payments()
        logging.info(f"Data fetched successfully, {data}")
        return jsonify(data), 200
    except Exception as e:
        logging.error(f"Error fetching payments: {e}")
        return jsonify({"error": str(e)}), 500

# Create new payment
@bp.route('/', methods=['POST'])
def create_payment():
    form_data = request.form
    data_dict = {key: value for key, value in form_data.items()}
    try:
        payments.create_payment(data_dict)
        return redirect(request.referrer)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Get payment by id
@bp.route('/<int:id>', methods=['GET'])
def get_payment(id):
    payment = payments.get_payment_by_id(id)
    if payment:
        return jsonify(payment.to_dict())
    return jsonify({"error": "Payment not found"}), 404

# Update payment by id
@bp.route('/update', methods=['POST'])
def update_payment():
    form_data = request.form
    data = {key: value for key, value in form_data.items()}
    payment_id = data['paymentId']
    payment = payments.update_payment(payment_id, data)
    if payment:
        return redirect(request.referrer)
    else:
        return jsonify({"error": "Payment not found"}), 404

# Delete payment by id
@bp.route('/delete', methods=['POST'])
def delete_payment():
    payment_id = request.form.get('paymentId')
    success = payments.delete_payment(payment_id)
    if success:
        return redirect(request.referrer)
    return jsonify({"error": "Payment not found"}), 404
