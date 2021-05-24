from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, SelectField
from wtforms.validators import InputRequired, URL, NumberRange

pet_options = ['Cat','Dog','Porcupine']

class AddPetForm(FlaskForm):
    """ form to add a new pet to the adoption agency """
    name = StringField('Pet Name', validators=[InputRequired()])
    species = SelectField('Species Type', choices=[(pet,pet) for pet in pet_options], validators=[InputRequired()])
    photo_url = StringField('Add picture (if applicable)', validators=[URL()])
    age = FloatField('Age', validators=[NumberRange(min=0,max=30)])
    notes = StringField('Additional notes about this animal')
    available = BooleanField('Available?')

class EditPetForm(FlaskForm):
    """ edit the details of a pet """
    photo_url = StringField('Update picture', validators=[URL()])
    age = FloatField('Age', validators=[NumberRange(min=0,max=30)])
    notes = StringField('Update Notes')
    available = BooleanField('Available?')