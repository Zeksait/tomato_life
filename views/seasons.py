from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.exceptions import NotFound, BadRequest

seasons_app = Blueprint('seasons_app', __name__)

SEASONS_DATA = {
    1: 'Winter',
    2: 'Spring',
    3: 'Summer',
    4: 'Autumn',
}


@seasons_app.route("/", endpoint='list')
def get_season_list():
    return render_template("seasons/list.html", seasons_list=SEASONS_DATA)


@seasons_app.route("/<int:season_id>/", endpoint='detail')
def get_season(season_id: int):
    season_name = SEASONS_DATA.get(season_id)
    if season_name is None:
        raise NotFound('Нет такого')
    return render_template("seasons/detail.html", season_id=season_id, season_name=season_name)


@seasons_app.route("/add/", methods=['GET', 'POST'], endpoint='add')
def create_season():
    if request.method == 'GET':
        return render_template('seasons/add.html')

    season_name = request.form.get("season-name")
    if not season_name:
        raise BadRequest('пусто')

    season_id = len(SEASONS_DATA) + 1
    SEASONS_DATA[season_id] = season_name
    return redirect(url_for('seasons_app.detail', season_id= season_id))