from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField

class AddPetForm(FlaskForm):
    """ form to add a new pet to the adoption agency """
    name = StringField('Pet Name')
    species = StringField('Species Type')
    photo_url = StringField('Add picture (if applicable)')
    age = FloatField('Age')
    notes = StringField('Additional notes about this animal')
    available = BooleanField('Available?')