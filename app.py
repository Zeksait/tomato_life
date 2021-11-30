import json
from flask import Flask, request, render_template
from flask_migrate import Migrate
from flask_crontab import Crontab
from werkzeug.exceptions import NotFound, BadRequest, InternalServerError
from sqlalchemy.exc import IntegrityError, DatabaseError

from models.database import db, History
from views.sensors import sensors_app

app = Flask(__name__)
crontab = Crontab(app)
app.register_blueprint(sensors_app, url_prefix="/sensors")
app.debug = True
app.config.update(
    SQLALCHEMY_DATABASE_URI="sqlite:///./database.db",
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)
db.init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def hello_world():
    print(request.path)
    return render_template("index.html", content='Test')


@app.route("/dashboard/")
def dashboard():
    moments = History.query.order_by(History.id).limit(10)  # Как выбрать последние 10?
    return render_template("dashboard/index.html", moments=moments)  # data_str=data_str


@crontab.job(hour="1")
def get_sensor_value_every_hour():  # параметры обновляются каждый час
    sensors = db.query.all()
    for sensor in sensors:
        res = sensor.get_sensor_value()
        moment = History(sensor_name=sensor.name, sensor_status=sensor.status, sensor_value=res)
        db.session.add(moment)
    try:
        db.session.commit()
    except IntegrityError:
        print("Could not add moment history, got integrity error")
        db.session.rollback()
        raise BadRequest("Error adding new moment history")
    except DatabaseError:
        print("Could not add product, got database error")
        db.session.rollback()
        raise InternalServerError("Error adding new moment history")

# last_ten_sensor_values = Sensor.query.order_by(Sensor.id.desc()).limit(10)
