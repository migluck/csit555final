from flask import Blueprint, jsonify, render_template
import socket

bp = Blueprint('health', __name__, url_prefix='/')


def fetch_details():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return str(hostname), str(ip)


@bp.route("/")
def hello_world():
    return "<p>Hello from Tax Calculation!</p>"


@bp.route("/health")
def health():
    return jsonify(
        status="UP"
    )


@bp.route("/details")
def details():
    hostname, ip = fetch_details()
    return render_template('index.html', HOSTNAME=hostname, IP=ip)