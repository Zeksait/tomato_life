from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.exceptions import NotFound, BadRequest, InternalServerError
from sqlalchemy.exc import IntegrityError, DatabaseError

from models.database import db
from models.sensor import Sensor


sensors_app = Blueprint('sensors_app', __name__)


@sensors_app.route("/", endpoint="list")
def get_products_list():
    sensors = Sensor.query.all()
    return render_template("sensors/list.html", sensors=sensors)


@sensors_app.route("/<int:sensor_id>/", endpoint='detail')
def get_sensor(sensor_id: int):
    sensor = Sensor.query.filter_by(id=sensor_id).one_or_none()
    if sensor is None:
        raise NotFound(f"Нет датчика с id {sensor_id}")

    if request.method == "GET":
        return render_template("sensors/detail.html", sensor=sensor, )


@sensors_app.route("/add/", methods=['GET', 'POST'], endpoint='add')
def add_sensor():
    if request.method == 'GET':
        return render_template('sensors/add.html')

    sensor_name = request.form.get("sensor-name")
    if not sensor_name:
        raise BadRequest('Не указано название сенсора')

    sensor_type = request.form.get("sensor-type")
    if not sensor_type:
        raise BadRequest("Укажите тип сенсора")

    sensor_type_connection = request.form.get("sensor-type_connection")
    if not sensor_type_connection:
        raise BadRequest("Укажите тип соединения")

    sensor_address = request.form.get("sensor-address")
    if not sensor_address:
        raise BadRequest("Укажите адрес порта")

    sensor_speed = request.form.get("sensor-speed")
    if not sensor_speed:
        raise BadRequest("Укажите скорость порта")

    sensor = Sensor(name=sensor_name, type=sensor_type, type_connection=sensor_type_connection,
                    port_address=sensor_address, port_speed=sensor_speed)

    db.session.add(sensor)
    try:
        db.session.commit()
    except IntegrityError:
        print("Could not add product, got integrity error")
        db.session.rollback()
        raise BadRequest("Error adding new product, probably the name is not unique")
    except DatabaseError:
        print("Could not add product, got database error")
        db.session.rollback()
        raise InternalServerError("Error adding new product")
