from ast import stmt
import email
from email.policy import default
from enum import unique
from unicodedata import name

import sqlalchemy
from . import db
from sqlalchemy.sql import func
from datetime import date



class Apartment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))




class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(150))
    phone_num = db.Column(db.String(150))
    check_in = db.Column(db.String(150))
    hour1 = db.Column(db.String(150))
    check_out = db.Column(db.String(150))
    hour2 = db.Column(db.String(150))
    person = db.Column(db.String(150))
    apartment_id = db.Column(db.Integer, db.ForeignKey('apartment.id'))
    

