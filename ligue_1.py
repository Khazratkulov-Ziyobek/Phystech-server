import scraping
from flask import render_template, Blueprint

ligue_1 = Blueprint('ligue_1', __name__, template_folder='templates')


@ligue_1.route('/ligue_1')
def results_table():
    create_table = scraping.create_table
    scraping.url = 'https://www.skysports.com/ligue-1-table'
    scraping.scraping()
    return render_template("ligue_1.html", create_table=create_table)
