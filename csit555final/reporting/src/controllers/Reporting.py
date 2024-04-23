import logging
import os
from flask import Blueprint, jsonify, render_template
import requests

bp = Blueprint('reporting', __name__, url_prefix='/reporting')
PAYMENT_RECORD_SERVICE_URL = os.getenv('PAYMENT_RECORD_SERVICE_URL')
@bp.route('/', methods=['GET'])
def index():
    try:
        response = requests.get(f"{PAYMENT_RECORD_SERVICE_URL}/payment/all")
        if response.status_code == 200:
            data = response.json()
            return render_template('index.html', payments=data)
        return jsonify({'message': f"Failed to get items from Service A {response.status_code}"})
    except Exception as e:
        logging.error(f"Error fetching payments: {e}")
        return jsonify({"error": str(e)}), 500

