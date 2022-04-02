from flask import render_template, url_for, request, redirect, flash
from flask_login import login_user, logout_user, login_required, current_user
from doorbell import app, db
from doorbell.models import User
from doorbell.forms import LoginForm

@app.route("/")

@app.route("/home")
def home():
   if current_user.is_authenticated:
      return render_template("home.html")
   else:
      return redirect(url_for("login"))
   
@app.route("/login", methods = ["GET", "POST"])
def login():
   form = LoginForm()
   errors = []
   if form.validate_on_submit():
      user = User.query.filter_by(username = form.username.data).first()
      if user is not None and user.verify_password(form.password.data):
         login_user(user)
         return redirect(url_for("home"))
      else: 
         errors.append("Invalid password.")
   for element in form:
      errors.extend(element.errors)
   return render_template("login.html", title = "login", form = form, errors = errors)

@app.route("/logout")
def logout():
   logout_user()
   return redirect(url_for("home"))