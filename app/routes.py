from flask import Flask, render_template, request, jsonify, current_app as app
from .scanner import scan_network

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    try:
        data = request.get_json()
        ip_range = data.get('ip_range')
        ports = data.get('ports')
        if not ip_range or not ports:
            return jsonify({'error': 'Invalid input'}), 400
        results = scan_network(ip_range, ports)
        return jsonify(results)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
