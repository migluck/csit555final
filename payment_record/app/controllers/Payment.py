from flask import Blueprint, request, jsonify, render_template
from app.services.payments import get_all_payment, create_payment

bp = Blueprint('payment', __name__, url_prefix='/payment')

@bp.route('/all', methods=['GET'])
def index():
    data = get_all_payment()
    return jsonify(data), 200

@bp.route('/', methods=['POST'])
def add_payment():
    payment_data = request.json
    payment = create_payment(payment_data)
    return jsonify(payment), 201


