import json
from flask import Flask, request, render_template
from flask_migrate import Migrate
from views.sensors import seasons_app
from flask_crontab import Crontab
from models.database import db
from views.sensors import sensors_app

app = Flask(__name__)
crontab = Crontab(app)
app.register_blueprint(sensors_app, url_prefix="/sensors")
app.debug = True


@app.route("/")
def hello_world():
    print(request.path)
    return render_template("index.html", content='Test')


@app.route("/dashboard/")
def hello_name():
    data_str = json.dumps(sensors_history)  # 10 last values
    return render_template("dashboard/index.html", data_str=data_str)


@crontab.job(hour="1")
def get_sensor_value_every_hour():
    sensors = db.query.all()
    for sensor in sensors:
        res = sensor.get_sensor_value()
        db.session.add()


last_ten_sensor_values = Sensor.query.order_by(Sensor.id.desc()).limit(10)