import scraping
from flask import render_template, Blueprint

premier_league = Blueprint('premier_league', __name__, template_folder='templates')


@premier_league.route('/premier_league')
def results_table():
    create_table = scraping.create_table
    scraping.url = 'https://www.skysports.com/premier-league-table'
    scraping.scraping()
    return render_template("premier_league.html", create_table=create_table)
