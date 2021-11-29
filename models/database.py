from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Sensor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    sensor_type = db.Column(db.String(20))  # command or read
    type_connection = db.Column(db.String(20))  # arduino etc.
    port_address = db.Column(db.String(20))  # com address
    port_speed = db.Column(db.String(20))  # 9600
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

