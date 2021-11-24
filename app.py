from flask import Flask, request, render_template
from models.database import db
from flask_migrate import Migrate
from views.seasons import seasons_app
from flask_crontab import Crontab
import random

app = Flask(__name__)
crontab = Crontab(app)
app.register_blueprint(seasons_app, url_prefix="/seasons")
app.config.update(
    SQLALCHEMY_DATABASE_URI="sqlite:///./seasons.db",
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)
db.init_app(app)
migrate = Migrate(app, db)
app.debug = True
data = []


@app.route("/")
def hello_world():
    print(request.path)
    return render_template("index.html", content='Test')


@app.route("/dashboard/")
def hello_name():
    return render_template("dashboard/index.html", data=data)


@crontab.job(minute="1", hour="0")
def my_scheduled_job():
    data.append(random.randint(0, 10))
    print(data)
