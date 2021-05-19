import scraping
from flask import render_template, Blueprint

bundesliga = Blueprint('bundesliga', __name__, template_folder='templates')


@bundesliga.route('/bundesliga')
def results_table():
    create_table = scraping.create_table
    scraping.url = 'https://www.skysports.com/bundesliga-table'
    scraping.scraping()
    return render_template("bundesliga.html", create_table=create_table)
