import json
from flask import Flask, request, render_template
from flask_migrate import Migrate
from views.seasons import seasons_app
from database import sensors_history

app = Flask(__name__)
app.register_blueprint(seasons_app, url_prefix="/seasons")
app.debug = True


@app.route("/")
def hello_world():
    print(request.path)
    return render_template("index.html", content='Test')


@app.route("/dashboard/")
def hello_name():
    data_str = json.dumps(sensors_history)
    return render_template("dashboard/index.html", data_str=data_str)
