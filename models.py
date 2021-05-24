from flask_sqlalchemy import SQLAlchemy

# set up the server and initialize
db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """ Modeling a pet that is potentially available for adoption """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, default='https://images.unsplash.com/photo-1543466835-00a7907e9de1?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1567&q=80')
    age = db.Column(db.Integer, default=1)
    notes = db.Column(db.Text, default='Doggo seeking new home!')
    available = db.Column(db.Boolean, default=True, nullable=False)

