from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_driver = db.Column(db.Boolean, default=False)

class Ride(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    passenger_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    driver_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)
    pickup = db.Column(db.String(200))
    drop = db.Column(db.String(200))
    status = db.Column(db.String(20), default="Pending")
