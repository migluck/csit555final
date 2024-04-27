import logging
import os
from flask import Blueprint, jsonify, render_template
import requests

bp = Blueprint('reporting', __name__, url_prefix='/')
PAYMENT_RECORD_INTERNAL_URL = os.getenv('PAYMENT_RECORD_INTERNAL_URL')
PAYMENT_RECORD_EXTERNAL_URL = os.getenv('PAYMENT_RECORD_EXTERNAL_URL')


@bp.route('/', methods=['GET'])
def all_payment():
    try:
        response = requests.get(f"{PAYMENT_RECORD_INTERNAL_URL}/payments")
        if response.status_code == 200:
            data = response.json()
            print(PAYMENT_RECORD_INTERNAL_URL)
            return render_template('allpayments.html', payments=data, PAYMENT_RECORD_INTERNAL_URL=PAYMENT_RECORD_INTERNAL_URL, PAYMENT_RECORD_EXTERNAL_URL=PAYMENT_RECORD_EXTERNAL_URL)
        return jsonify({'message': f"Failed to get items from Service A {response.status_code}"})
    except Exception as e:
        logging.error(f"Error fetching payments: {e}")
        return jsonify({"error": str(e)}), 500
@bp.route('/dashboard', methods=['GET'])
def home():
    return render_template('home.html')

@bp.route('/add', methods=['GET'])
def add_payment():
    return render_template('addpayment.html', PAYMENT_RECORD_EXTERNAL_URL=PAYMENT_RECORD_EXTERNAL_URL)

