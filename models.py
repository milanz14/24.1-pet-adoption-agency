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
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, default=True)

