from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

from connections.arduino import get_value

db = SQLAlchemy()




class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    sensor_name = db.Column()  # from sensor object
    sensor_status = db.Column()  # from sensor object
    sensor_value = db.Column(db.Float())
