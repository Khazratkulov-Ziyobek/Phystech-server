from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from premier_league import premier_league
from la_liga import la_liga
from bundesliga import bundesliga
from serie_a import serie_a
from ligue_1 import ligue_1

app = Flask(__name__)
app.register_blueprint(premier_league)
app.register_blueprint(la_liga)
app.register_blueprint(bundesliga)
app.register_blueprint(serie_a)
app.register_blueprint(ligue_1)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Database(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.Text)
    surname = db.Column(db.Text)
    country = db.Column(db.Text)
    group_num = db.Column(db.Text)

    def __repr__(self):
        return '<Database %r>' % self.id


@app.route('/')
@app.route('/home')
def home_page():
    all_data = Database.query.all()
    return render_template('home.html', all_data=all_data)


@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        info = (
            request.form['firstname'],
            request.form['surname'],
            request.form['country'],
            request.form['group_num']
        )
        new_data = Database(firstname=info[0], surname=info[1], country=info[2], group_num=info[3])
        db.session.add(new_data)
        db.session.commit()
        return render_template("add_success.html")
    else:
        return render_template("add_student.html")


@app.route('/scraping')
def scraping():
    return render_template("scraping.html")


if __name__ == '__main__':
    app.run(debug=True)
