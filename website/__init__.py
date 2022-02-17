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

db = SQLAlchemy()
DB_NAME = "database.db"


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




def create_database(app):
    if not path.exists('Flask-web-app-apartmani/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database')

def insert_into(app, Apartment):
    with app.app_context():
        ApartmentA1 = Apartment(id=2022112, name='Apartment A1')
        ApertmentA2 = Apartment(id=2022123, name='Apartment A2')
        db.session.add_all([ApartmentA1, ApertmentA2])
        db.session.commit()






"""
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/book-now", methods=['GET', 'POST'])
def book():
    data = request.form
    print(data)
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone_num = request.form.get('phone_num')
        person = request.form.get('person')
        check_in = request.form.get('check_in')
        hour1 = request.form.get('hour1')
        check_out = request.form.get('check_out')
        hour2 = request.form.get('hour2')
        apartment = request.form.get('apartment')

        if len(email) < 4:
            flash('Email is too short.', category='error')
        elif len(name) < 2:
            flash('Name must be greather then 1 character', category='error')
        else:
            flash('Rezervacija zaprimljena', category='success')
            pass


    return render_template("book-now.html")
            
@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/book-now/checkout", methods=['GET', 'POST'])
def checkout():
    return render_template("checkout.html")
"""

    





