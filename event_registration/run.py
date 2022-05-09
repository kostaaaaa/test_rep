from datetime import datetime

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'awdawdawrnjn45345nkjn345n3jk45n'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
now = datetime.now()


class Guest(db.Model):
    __tablename__ = 'Guests'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(500), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, default=now.strftime("%d/%m/%Y, %H:%M:%S"))


@app.route('/main')
@app.route('/')
def index():      
    return render_template('index.html', title='Main')


@app.route('/guests', methods=['GET'])
def guests():
    info = []
    try:
        info = Guest.query.all()
        return render_template('guests.html', title='Guests', list=info)
    
    except Exception:
        print('[POSTGRESQL] Error reading DB!')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        try:
            guest = Guest(name=request.form['name'], surname=request.form['surname'], age=request.form['age'])
            
            db.session.add(guest)
            db.session.flush()
            db.session.commit()
            
            print('[POSTGRESQL] Data was added successfully! :)')
        
        except Exception:
            db.session.rollback()
            print('[POSTGRESQL] Data was not added!!!')

    return render_template('registration.html', title="Registration")


if __name__ == '__main__':
    app.run(debug=True)
