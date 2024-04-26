import logging
import os
from flask import Blueprint, jsonify, render_template
import requests

bp = Blueprint('reporting', __name__, url_prefix='/reporting')
PAYMENT_RECORD_SERVICE_URL = os.getenv('PAYMENT_RECORD_SERVICE_URL')
# @bp.route('/', methods=['GET'])
# def index():
#     try:
#         response = requests.get(f"{PAYMENT_RECORD_SERVICE_URL}/payment/all")
#         if response.status_code == 200:
#             data = response.json()
#             return render_template('index.html', payments=data)
#         return jsonify({'message': f"Failed to get items from Service A {response.status_code}"})
#     except Exception as e:
#         logging.error(f"Error fetching payments: {e}")
#         return jsonify({"error": str(e)}), 500

@bp.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@bp.route('/add', methods=['GET'])
def add_payment():
    return render_template('addpayment.html')

@bp.route('/all', methods=['GET'])
def all_payment():
    try:
        response = requests.get("http://127.0.0.1:5000/payments")
        if response.status_code == 200:
            data = response.json()
            return render_template('allpayments.html', payments=data)
            # return render_template('index.html', payments=data)
        return jsonify({'message': f"Failed to get items from Service A {response.status_code}"})
    except Exception as e:
        logging.error(f"Error fetching payments: {e}")
        return jsonify({"error": str(e)}), 500
