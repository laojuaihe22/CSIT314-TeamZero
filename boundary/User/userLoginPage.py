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
    verifyUser, user_role, user_id = loginController.verifyAccount(user_email, user_pass)
    
    if verifyUser:
        session["id"] = user_id
        session["user_email"] = user_email.lower()
        session["roles"] = user_role  
        print(user_id)
        return redirect(url_for('login_app.displayHomePage'))
    else:
        flash('Invalid email or password', 'error')     
        return redirect(url_for('login_app.displayLoginPage'))

@login_app.route("/home", methods=["GET"])
def displayHomePage():
    if "user_email" in session:
        if session['roles'] == "admin":
            return render_template('adminDashboard.html')
        elif session['roles'] == "rea":
            return render_template("realEstateAgentDashboard.html")
        elif session['roles'] == "buyer":
            return render_template("buyerDashboard.html")   
        elif session['roles'] == "seller":
            return render_template("sellerDashboard.html")
    else:
        flash("You need to log in first", 'error')
        return redirect(url_for('login_app.displayLoginPage'))
