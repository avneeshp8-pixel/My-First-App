from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    is_driver = BooleanField("Register as Driver")
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

class RideForm(FlaskForm):
    pickup = StringField("Pickup Location", validators=[DataRequired()])
    drop = StringField("Drop Location", validators=[DataRequired()])
    submit = SubmitField("Book Ride")
