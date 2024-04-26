from flask import Blueprint, request, jsonify, render_template
from src.services  import payments
import logging

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
    data = request.get_json()
    try:
        new_payment = payments.create_payment(data)
        return jsonify(new_payment.to_dict()), 201
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
@bp.route('/<int:id>', methods=['PUT'])
def update_payment(id):
    data = request.get_json()
    payment = payments.update_payment(id, data)
    if payment:
        return jsonify(payment.to_dict())
    else:
        return jsonify({"error": "Payment not found"}), 404

# Delete payment by id
@bp.route('/<int:id>', methods=['DELETE'])
def delete_payment(id):
    success = payments.delete_payment(id)
    if success:
        return jsonify({"success": "Payment deleted"}), 200
    return jsonify({"error": "Payment not found"}), 404

