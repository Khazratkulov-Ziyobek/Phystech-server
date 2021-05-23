import scraping
from flask import render_template, Blueprint

serie_a = Blueprint('serie_a', __name__, template_folder='templates')


@serie_a.route('/serie_a')
def results_table():
    create_table = scraping.create_table
    scraping.url = 'https://www.skysports.com/serie-a-table'
    scraping.scraping()
    return render_template("serie_a.html", create_table=create_table)
