from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
#add for imports here as we build out forms

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption_agency'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =  False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'development_key'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)