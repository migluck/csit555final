from flask import Blueprint, request, jsonify, render_template
from src.services.payments import get_all_payment, create_payment
import logging

bp = Blueprint('payment', __name__, url_prefix='/payment')


@bp.route('/all', methods=['GET'])
def index():
    logging.info("Fetching all payments")
    try:
        data = get_all_payment()
        logging.info(f"Data fetched dsadsa successfully, {data}")
        return jsonify(data), 200
    except Exception as e:
        logging.error(f"Error fetching payments: {e}")
        return jsonify({"error": str(e)}), 500

@bp.route('/', methods=['POST'])
def add_payment():
    data = request.get_json()
    payment = create_payment(data)
    return jsonify(payment.to_dict()), 201


