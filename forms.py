from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

CITIES = [
    ('Delhi', 'Delhi'),
    ('Mumbai', 'Mumbai'),
    ('Kolkata', 'Kolkata'),
    ('Chennai', 'Chennai'),
    ('Bangalore', 'Bangalore'),
    ('Hyderabad', 'Hyderabad'),
    ('Ahmedabad', 'Ahmedabad'),
    ('Pune', 'Pune'),
    ('Jaipur', 'Jaipur'),
    ('Lucknow', 'Lucknow'),
    ('Kanpur', 'Kanpur'),
    ('Nagpur', 'Nagpur'),
    ('Indore', 'Indore'),
    ('Bhopal', 'Bhopal'),
    ('Patna', 'Patna'),
    ('Ludhiana', 'Ludhiana'),
    ('Agra', 'Agra'),
    ('Nashik', 'Nashik'),
    ('Vadodara', 'Vadodara'),
    ('Varanasi', 'Varanasi'),
    # ...aur bhi cities add kar sakte hain...
]

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=150)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=3)])
    is_driver = BooleanField('Register as Driver')
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RideForm(FlaskForm):
    pickup = SelectField('Pickup Location', choices=CITIES, validators=[DataRequired()])
    drop = SelectField('Drop Location', choices=CITIES, validators=[DataRequired()])
    submit = SubmitField('Book Ride')