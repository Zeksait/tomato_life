from flask import Flask, request, render_template
from models.database import db
from flask_migrate import Migrate
from views.seasons import seasons_app

app = Flask(__name__)
app.register_blueprint(seasons_app, url_prefix="/seasons")
app.config.update(
    SQLALCHEMY_DATABASE_URI="sqlite:///./seasons.db",
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)
db.init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def hello_world():
    print(request.path)
    return render_template("index.html", content='Test')


@app.route("/dashboard/")
def hello_name():
    return render_template("dashboard/index.html", content='Test')
