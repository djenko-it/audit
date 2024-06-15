from flask import render_template, request, jsonify, current_app as app
from .scanner import scan_network

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    data = request.get_json()
    ip_range = data.get('ip_range')
    ports = data.get('ports')
    results = scan_network(ip_range, ports)
    return jsonify(results)
