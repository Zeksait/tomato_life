from models.database import db
from datetime import datetime
from sqlalchemy import func
from connections.arduino import get_value


class Sensor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    type = db.Column(db.String(20), nullable=False)  # send or read
    status = db.Column(db.Boolean, default=False)
    type_connection = db.Column(db.String(20), nullable=False)  # arduino etc.
    port_address = db.Column(db.String(20))  # com port
    port_speed = db.Column(db.Integer)  # port speed
    created_at = db.Column(db.DateTime, default=datetime.utcnow, server_default=func.now(),)

    def get_sensor_value(self):
        return get_value(self.port_address, self.port_speed)
