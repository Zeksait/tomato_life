from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from connections.arduino import get_value

db = SQLAlchemy()


class Sensor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    type = db.Column(db.String(20))  # send or read
    status = db.Column(db.Boolean, default=False)
    type_connection = db.Column(db.String(20))  # arduino etc.
    port_address = db.Column(db.String(20))  # com port
    port_speed = db.Column(db.Integer)  # port speed
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def get_sensor_value(self):
        return get_value(self.port_address, self.port_speed)


class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    sensor_name = db.Column()  # from sensor object
    sensor_status = db.Column()  # from sensor object
    sensor_value = db.Column(db.Float())
