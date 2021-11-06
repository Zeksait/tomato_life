from flask import Flask, request

app = Flask(__name__)


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