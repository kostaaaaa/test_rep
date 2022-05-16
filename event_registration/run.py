from datetime import datetime

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'awdawdawrnjn45345nkjn345n3jk45n'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
now = datetime.now()


event_guest = db.Table('event_guests',
    db.Column('event_id', db.Integer, db.ForeignKey('events.id')),
    db.Column('guest_id', db.Integer, db.ForeignKey('guests.id'))
)


class Event(db.Model):
    __tablename__ = 'events'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    guests = db.relationship('Guest', lazy='dynamic', secondary=event_guest, backref=db.backref('events', lazy='dynamic'))


class Guest(db.Model):
    __tablename__ = 'guests'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(500), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, default=now.strftime("%d/%m/%Y, %H:%M:%S"))


@app.route('/main', methods=['GET'])
@app.route('/', methods=['GET'])
def index():      
    return render_template('index.html', title='Main')


@app.route('/events', methods=['GET'])
@app.route('/events/', methods=['GET'])
def events():
    events = Event.query.all()
    return render_template('events.html', title='Events', events=events)


@app.route('/events/<int:event_id>', methods=['GET', 'POST'])
def register(event_id):
    event = Event.query.get(event_id)
    if request.method == 'POST':
        guest = Guest.query.filter_by(
        name=request.form['name'],
        surname=request.form['surname'],
        age=request.form['age'],
        ).first()

        if not guest:
            guest = Guest(
                name=request.form['name'],
                surname=request.form['surname'],
                age=request.form['age'],
            )
            db.session.add(guest)
            db.session.commit()

        else:
            event.guests.append(guest)
            db.session.add(event)
            db.session.commit()
        
        print('[POSTGRESQL] Data was added successfully! :)')


    return render_template('register.html', event=event, title="Event registration")



@app.route('/add_event', methods=['GET', 'POST'])
def add_event():
    if request.method == 'POST':
        try:

            event = Event(name=request.form['name'], description=request.form['description'], date=request.form['date'])
            
            db.session.add(event)
            db.session.flush()
            db.session.commit()
            
            print('[POSTGRESQL] Data was added successfully! :)')
        except Exception:
            db.session.rollback()
            print('[POSTGRESQL] Data was not added!!!')

    return render_template('add_event.html', title="Add event")


if __name__ == '__main__':
    app.run(debug=True)
