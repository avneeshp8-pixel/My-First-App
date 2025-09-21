import os
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "avneesh"
    SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

from models import db, User, Ride
from forms import RegisterForm, LoginForm, RideForm

app = Flask(__name__, template_folder="templates", static_folder="static")
app.config.from_object(Config)

db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_pw = generate_password_hash(form.password.data)
        user = User(username=form.username.data, password=hashed_pw, is_driver=form.is_driver.data)
        db.session.add(user)
        db.session.commit()
        flash("Registered successfully! Please login.", "success")
        return redirect(url_for("login"))
    return render_template("register.html", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for("dashboard"))  # yahan redirect karein
        else:
            flash("Invalid credentials", "danger")
    return render_template("login.html", form=form)

@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html", user=current_user)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/book", methods=["GET", "POST"])
@login_required
def book():
    if current_user.is_driver:
        flash("Drivers cannot book rides.", "danger")
        return redirect(url_for("index"))
    form = RideForm()
    if form.validate_on_submit():
        ride = Ride(passenger_id=current_user.id, pickup=form.pickup.data, drop=form.drop.data)
        db.session.add(ride)
        db.session.commit()
        flash("Ride booked successfully!", "success")
        return redirect(url_for("status", ride_id=ride.id))
    return render_template("book_ride.html", form=form)

@app.route("/status/<int:ride_id>")
@login_required
def status(ride_id):
    ride = Ride.query.get_or_404(ride_id)
    # Fare calculation based on city pair
    city_fares = {
        ("Delhi", "Mumbai"): 2500,
        ("Delhi", "Kolkata"): 2200,
        ("Delhi", "Chennai"): 2700,
        ("Mumbai", "Pune"): 500,
        ("Kolkata", "Patna"): 800,
        ("Bangalore", "Chennai"): 900,
        # ...aur bhi city pairs add kar sakte hain...
    }
    # Default fare if pair not found
    fare = city_fares.get((ride.pickup, ride.drop), 1200)
    return render_template("ride_status.html", ride=ride, fare=fare)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
