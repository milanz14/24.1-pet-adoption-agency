from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption_agency'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =  False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'development_key'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def homepage():
    """ show the homepage which shows list
    of all available pets """
    pets = Pet.query.all()
    return render_template('index.html', pets=pets)

@app.route('/add', methods=['GET','POST'])
def add_new_pet():
    """ render the new pet form """
    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data

        try: 
            new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes,available=available)
            db.session.add(new_pet)
            db.session.commit()
        except:
            flash('Something went wrong')
            return redirect('/')
        flash('Pet added!')
        return redirect('/')
    else:
        return render_template('addpetform.html', form=form)

@app.route('/<int:pet_id>')
def show_pet_details(pet_id):
    """ show a details page for each specific pet """
    pet = Pet.query.get_or_404(pet_id)
    return render_template('petdetails.html', pet=pet)

@app.route('/<int:pet_id>/edit', methods=['GET','POST'])
def edit_pet_details(pet_id):
    """ edit the details of a specific pet """
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm()

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        flash(f'{pet.name} has been updated!')
        return redirect(f'/{pet.id}')
    else:
        return render_template('editpet.html', form=form, pet=pet)