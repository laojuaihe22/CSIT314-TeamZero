from flask import Blueprint, redirect, render_template, request, session, flash, url_for
from controller.User.loginController import LoginController

login_app = Blueprint('login_app', __name__)

@login_app.route("/", methods=["GET"])
def displayLoginPage():
    if "user_email" in session:
        session.permanent = True
        return redirect(url_for('login_app.displayHomePage'))
    else:
        return render_template("login.html")

@login_app.route("/", methods=["POST"])
def processLoginPage():
    user_email = request.form["email"]
    user_pass = request.form["password"]
    
    loginController = LoginController()
    verifyUser, user_role = loginController.verifyAccount(user_email, user_pass)
    
    if verifyUser:
        session["user_email"] = user_email
        session["roles"] = user_role  
        return redirect(url_for('login_app.displayHomePage'))
    else:
        flash('Invalid email or password', 'error')     
        return redirect(url_for('login_app.displayLoginPage'))

@login_app.route("/home", methods=["GET"])
def displayHomePage():
    if "user_email" in session:
        role = session['roles']
        if role == "admin":
            return render_template('HomeProfile.html', email=session["user_email"])
        else:
            return render_template("home.html", role=role)
    else:
        flash("You need to log in first", 'error')
        return redirect(url_for('login_app.displayLoginPage'))

@login_app.route("/home", methods=["GET"])
def displayHomePage():
    if "user_email" in session:
        role = session['roles']
        if role == "admin":
            return render_template('adminDashboard.html')
        else:
            return render_template("home.html", role=role)
    else:
        flash("You need to log in first", 'error')
        return redirect(url_for('login_app.displayLoginPage'))