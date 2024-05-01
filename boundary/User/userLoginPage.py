from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.loginController import LoginController

login_app = Blueprint('login_app', __name__)

@login_app.route("/", methods=["POST", "GET"])
def displayLoginPage():
    if "user_email" in session:
        return redirect('/logout')
    if request.method == "POST":
        user_email = request.form["email"]
        user_pass = request.form["password"]
        
        loginController = LoginController()
        verifyUser = loginController.verifyAccount(user_email, user_pass)
        
        
        if verifyUser:
            session.permanent = True
            session["user_email"] = user_email
            session["roles"] = loginController.getUserRole()  # Example roles assignment, adjust as needed
            # flash('Logged in successfully!', category='success')
            return redirect('/home/' + user_email)
        else:
            flash('Invalid email or password', 'error')
            return redirect('/')  # Allow user to retry login
    else:
        return render_template("login.html")
    
@login_app.route("/home/<userEmail>", methods=["GET"])
def displayHomePage(userEmail):
    if session["roles"] == "admin":
        return render_template("home.html", role=session["roles"])
    elif session["roles"] == "rea":
        return render_template("home.html", role="Real Estate Agent")
    elif session["roles"] == "buyer":
        return render_template("home.html", role=session["roles"])
    elif session["roles"] == "seller":
        return render_template("home.html", role=session["roles"])
    return False  