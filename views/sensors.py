from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.exceptions import NotFound, BadRequest

sensors_app = Blueprint('sensors_app', __name__)


@seasons_app.route("/", endpoint='list')
def get_season_list():
    return render_template("sensors/list.html")


@seasons_app.route("/<int:season_id>/", endpoint='detail')
def get_season(season_id: int):
    return True


@seasons_app.route("/add/", methods=['GET', 'POST'], endpoint='add')
def create_season():
    if request.method == 'GET':
        return render_template('seasons/add.html')

    season_name = request.form.get("season-name")
    if not season_name:
        raise BadRequest('пусто')
