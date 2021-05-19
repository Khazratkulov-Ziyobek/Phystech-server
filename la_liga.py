import scraping
from flask import render_template, Blueprint

la_liga = Blueprint('la_liga', __name__, template_folder='templates')


@la_liga.route('/la_liga')
def results_table():
    create_table = scraping.create_table
    scraping.url = 'https://www.skysports.com/la-liga-table'
    scraping.scraping()
    return render_template("la_liga.html", create_table=create_table)
