from flask import Blueprint, render_template
from utils import get_title, get_film_year, get_rating, get_genre


main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

@main_blueprint.route('/movie/<title>')
def title_info(title):
    info = get_title(title)
    return render_template('title_info.html', info=info)


@main_blueprint.route('/movie/<int:year>/to/<int:years>')
def film_year(year, years):
    posts = get_film_year(year, years)
    return render_template('film_year.html', posts=posts)


@main_blueprint.route('/rating/<type>')
def film_rating(type):
    posts = get_rating(type)
    return render_template('get_rating.html', posts=posts)


@main_blueprint.route('/genre/<genre>')
def film_genre(genre):
    posts = get_genre(genre)
    return render_template('get_genre.html', posts=posts)