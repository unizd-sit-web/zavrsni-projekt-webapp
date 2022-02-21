from email import message
from locale import format_string
from time import strftime
from unicodedata import name
from flask import Flask, flash, render_template, request, redirect, url_for
from flask_mail import Mail, Message
from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, BooleanField, HiddenField, DateField, validators, TextAreaField, EmailField, SelectField
from wtforms.validators import DataRequired, Email, InputRequired
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import insert, String, Column, DateTime, Date
from os import path
from sqlalchemy.sql import func

#app
app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'sdgsdsgsdgs asfasfasdfa'

#sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Reservation.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)


#konfiguracija flask maila
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'marko.kokioc@gmail.com'
app.config['MAIL_PASSWORD'] = 'markokokioc12'
mail = Mail(app)

#db model
class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    check_in = db.Column(db.Date())
    check_out = db.Column(db.Date())
    adults = db.Column(db.String(150))
    children = db.Column(db.String(150))
    apartment = db.Column(db.String(150))
    name_booking = db.Column(db.String(150))
    email_booking = db.Column(db.String(150))
    time_created = db.Column(db.String(150))
    paid = db.Column(db.String(150))

#booknow FlaskForm
APARTMENT_CHOICES = [('Apartment A1', 'A1'), ('Apartment A2', 'A2')]
class ReservationForm(FlaskForm):
    check_in=DateField("Arrival Date",  [validators.DataRequired("Select Arrival Date")], format='%Y-%m-%d')
    check_out=DateField("Departure Date",  [validators.DataRequired("Select Departure Date")], format='%Y-%m-%d')
    adults = StringField("Adults", [validators.DataRequired("No of Adults travelling are Mandatory!")])
    apartment = SelectField('Choose Apartment', [validators.DataRequired("Choose at least one Apartment")], choices=APARTMENT_CHOICES)
    children = StringField("Children")
    name_booking = StringField("Name",[validators.DataRequired("First Name is Mandatory!")])
    email_booking = EmailField("email",[validators.DataRequired("Email is Mandatory!")])
    submit = SubmitField("Send")


def sendContactForm(result):
    msg = Message("Contact Form from Lavander Apartments", sender="testing@web-design-johannesburg.com", recipients=["marko.kokioc@gmail.com"])
    msg.body = """
    Hello there,

    You just received a contact form.

    Name: {}
    Email: {}
    Subject: {}
    Message: {}
    
    
    regards,
    Webmaster
    
    """.format(result['name'], result['email'], result['subject'], result['message'])
    mail.send(msg)

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        result = {}

        result['name'] = request.form.get('name')
        result['email'] = request.form.get('email').replace(' ', '')
        result['subject'] = request.form.get('subject')
        result['message'] = request.form.get('message')

        sendContactForm(result)
        return redirect(url_for('.contact_thanks'))
    return render_template("contact.html")

#Upisi u bazu podataka novu rezervaciju
@app.route("/book-now", methods=['GET', 'POST'])
def book():
    form = ReservationForm()
    if form.validate_on_submit():
        name_booking = form.name_booking.data
        email_booking = form.email_booking.data
        apartment = form.apartment.data
        adults = form.adults.data
        children = form.children.data
        check_in = form.check_in.data
        check_out = form.check_out.data
        time_created = strftime("%m/%d/%Y, %H:%M:%S")
        paid = "not paid"
        new_reservation = Reservation(name_booking = name_booking, email_booking=email_booking, apartment=apartment, adults=adults, children=children, check_in=check_in, check_out=check_out, time_created=time_created, paid=paid)
        db.session.add(new_reservation)
        db.session.commit()
        return redirect(url_for('.checkout'))
    return render_template("book-now.html", form=form)

@app.route('/book-now/checkout', methods=['GET', 'POST'])
def checkout():
    obj = Reservation.query.all()
    id = str(obj[-1].id)
    name_to_update = Reservation.query.get_or_404(id)
    email_guest = Reservation.query.get_or_404(id)
    #Pošalji potvrdu rezervacije na mail.
    #Napravi Update baze podataka jer je rezervacija plaćena
    if request.method == 'POST':
        name_to_update.paid = "paid"
        db.session.commit()
        msg = Message('Confirmation', sender='marko.kokioc@gmail.com', recipients=[email_guest.email_booking])
        msg.body = 'Thank you for your reservation!'
        mail.send(msg) 
        return redirect(url_for('.thanks'))
    return render_template("checkout.html")

@app.route("/book-now/checkout/thanks")
def thanks():

    return render_template("thanks.html")

@app.route("/contact/thanks")
def contact_thanks():

    return render_template("thanks_contact.html")


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
