from flask_sqlalchemy import SQLAlchemy

# set up the server and initialize
db = SQLAlchemy()
def connect_db(app):
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """ Modeling a pet that is potentially available for adoption """
      