from flask import Flask, request
from models.database import db

app = Flask(__name__)
app.config.update(
    SQLALCHEMY_DATABASE_URI='"sqlite:///./seasons.db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)
db.init_app(app)


@app.route("/")
def hello_world():
    print(request.path)
    return "<p>HELLO, WORLD!</p>"


@app.route("/hello/")
def hello_name():
    name = request.args.get('name', 'world')
    return {
        "message": f"Hello {name}"
    }