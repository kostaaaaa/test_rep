import re
from datetime import datetime

from flask import Flask, flash, render_template, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash


app = Flask(__name__)
app.config['SECRET_KEY'] = 'awdawdawrnjn45345nkjn345n3jk45n'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

reg_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(500), nullable=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    pr = db.relationship('Profile', backref='user', uselist=False)


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    age = db.Column(db.Integer)
    city = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


@app.route('/')
def index():
    info = []
    try:
        info = User.query.all()
        return render_template('index.html', title='Main', list=info)

    except:
        print('[POSTGRESQL] Error reading DB!')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        if len(request.form['username']) < 3:
            flash('Length of name is too short')
        elif not (re.fullmatch(reg_email, request.form['email'])):
            flash('Your email is not valid!')
        elif not request.form['message']:
            flash('Input your message please!')
        else:
            flash('{a} , thanx for your message!'.format(a=request.form['username']))

    return render_template('contact.html', title='contact')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            hash = generate_password_hash(request.form['password'])
            user = User(email=request.form['email'], password=hash)
            db.session.add(user)
            db.session.flush()

            p = Profile(name=request.form['name'], age=request.form['age'],
                        city=request.form['city'], user_id = user.id)
            db.session.add(p)
            db.session.commit()
            print('[POSTGRESQL] Data was added successfully! :)')
        except:
            db.session.rollback()
            print('[POSTGRESQL] Data was not added!!!')

    return render_template('register.html', title="Registration")


if __name__ == '__main__':
    app.run(debug=True)
