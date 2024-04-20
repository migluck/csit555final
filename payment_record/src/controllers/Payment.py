from flask import Blueprint, request, jsonify, render_template
from src.services.payments import get_all_payment, create_payment
import logging

bp = Blueprint('payment', __name__, url_prefix='/payment')


@bp.route('/all', methods=['GET'])
def index():
    logging.log("Fetching all payments")
    try:
        data = get_all_payment()
        logging.info("Data fetched successfully")
        return jsonify(data), 200
    except Exception as e:
        logging.error(f"Error fetching payments: {e}")
        return jsonify({"error": str(e)}), 500

# def index():
#     data = get_all_payment()
#     print(data)
#     return jsonify(data), 200
    # return "Payment"

@bp.route('/', methods=['POST'])
def add_payment():
    payment_data = request.json
    payment = create_payment(payment_data)
    return jsonify(payment), 201


