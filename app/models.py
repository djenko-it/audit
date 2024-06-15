from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSONB

db = SQLAlchemy()

class ScanResult(db.Model):
    __tablename__ = 'scan_results'

    id = db.Column(db.Integer, primary_key=True)
    ip_range = db.Column(db.String, nullable=False)
    ports = db.Column(db.String, nullable=False)
    scan_type = db.Column(db.String, nullable=False)
    results = db.Column(JSONB, nullable=False)
    scan_date = db.Column(db.DateTime, default=db.func.current_timestamp())

    def to_dict(self):
        return {
            'id': self.id,
            'ip_range': self.ip_range,
            'ports': self.ports,
            'scan_type': self.scan_type,
            'results': self.results,
            'scan_date': self.scan_date
        }
