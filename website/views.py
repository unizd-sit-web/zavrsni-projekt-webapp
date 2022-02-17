from datetime import date
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Apartment, Reservation
from . import db

views = Blueprint('views', __name__)


@views.route("/home")
def home():
    return render_template("index.html")

@views.route("/about")
def about():
    return render_template("about.html")

@views.route("/gallery")
def gallery():
    return render_template("gallery.html")

@views.route("/book-now", methods=['GET', 'POST'])
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
        apartment_id = request.form.get('apartment_id')
        
        

        if len(email) < 4:
            flash('Email is too short.', category='error')
        elif len(name) < 2:
            flash('Name must be greather then 1 character', category='error')
        else:
            new_reservation = Reservation(name=name, email=email, phone_num=phone_num, check_in=check_in, hour1=hour1, check_out=check_out, hour2=hour2, person=person, apartment_id=apartment_id)
            db.session.add(new_reservation)
            db.session.commit()
            flash('Rezervacija zaprimljena', category='success')
            return redirect(url_for('.checkout'))
            


    return render_template("book-now.html")
            
@views.route("/contact")
def contact():

    return render_template("contact.html")

@views.route("/book-now/checkout", methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        return redirect(url_for('.thanks'))
    return render_template("checkout.html")

@views.route("book-now/checkout/thanks")
def thanks():

    return render_template("thanks.html")





    
    