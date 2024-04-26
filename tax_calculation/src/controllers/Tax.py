import logging
import os
from flask import Blueprint, jsonify
import requests

bp = Blueprint('tax', __name__, url_prefix='/tax')
PAYMENT_RECORD_SERVICE_URL = os.getenv('PAYMENT_RECORD_SERVICE_URL')
def calculate_tax(data):
    # Some formulas or equations to calculate taxes
    return data

@bp.route('/', methods=['GET'])
def index():
    try:
        response = requests.get(f"{PAYMENT_RECORD_SERVICE_URL}/payment/all")
        if response.status_code == 200:
            data = jsonify(response.json())
            data = calculate_tax(data)
            return data, 200
        return jsonify({'message': f"Failed to get items from Service A {response.status_code}"})
    except Exception as e:
        logging.error(f"Error fetching payments: {e}")
        return jsonify({"error": str(e)}), 500

