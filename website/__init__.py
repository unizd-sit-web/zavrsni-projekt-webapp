import email
from genericpath import exists
import imp
from inspect import Parameter
from tokenize import Number
from unicodedata import name
from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from os import path
from sqlalchemy import insert



#inicijalizacija baze podataka
db = SQLAlchemy()
DB_NAME = "database.db"

#Funkcija za izradu aplikacije
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sdgsdsgsdgs asfasfasdfa'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    from .models import Reservation, Apartment
    
    create_database(app)

    return app



#Funkcija za izradu baze podataka ako vec ne postoji
def create_database(app):
    if not path.exists('Flask-web-app-apartmani/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database')
#unos podataka u tablicu(apartman)
def insert_into(app, Apartment):
    with app.app_context():
        ApartmentA1 = Apartment(id=2022112, name='Apartment A1')
        ApertmentA2 = Apartment(id=2022123, name='Apartment A2')
        db.session.add_all([ApartmentA1, ApertmentA2])
        db.session.commit()
        




