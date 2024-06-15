from flask import Flask, render_template, request, jsonify
from .scanner import scan_network
from .models import db, ScanResult

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    try:
        data = request.get_json()
        ip_range = data.get('ip_range')
        ports = data.get('ports')
        scan_type = data.get('scan_type')
        if not ip_range or not ports or not scan_type:
            return jsonify({'error': 'Invalid input'}), 400
        results = scan_network(ip_range, ports, scan_type)
        save_scan_result(ip_range, ports, scan_type, results)
        return jsonify(results)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/scan/history', methods=['GET'])
def scan_history():
    scans = ScanResult.query.order_by(ScanResult.scan_date.desc()).all()
    return jsonify([scan.to_dict() for scan in scans])

def save_scan_result(ip_range, ports, scan_type, results):
    scan_result = ScanResult(ip_range=ip_range, ports=ports, scan_type=scan_type, results=results)
    db.session.add(scan_result)
    db.session.commit()
