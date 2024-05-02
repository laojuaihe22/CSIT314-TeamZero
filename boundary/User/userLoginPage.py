from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.User.loginController import LoginController

login_app = Blueprint('login_app', __name__)

@login_app.route("/", methods=["POST", "GET"])
def displayLoginPage():
    if request.method == "POST":
        user_email = request.form["email"]
        user_pass = request.form["password"]
        
        loginController = LoginController()
        verifyUser, user_role = loginController.verifyAccount(user_email, user_pass)
        
        if verifyUser:
            session["user_email"] = user_email
            session["roles"] = user_role  
            flash(f'{session["roles"]} have Logged in successfully!', 'success')
            return redirect('/home')
        else:
            flash('Invalid email or password', 'error')     
            return redirect('/')  # Allow user to retry login
    else:
        return render_template("login.html")
    
@login_app.route("/home", methods=["GET"])
def displayHomePage():
    
    if "user_email" in session:
        if session["roles"] == "admin":
            return render_template('admin.html',email=session["user_email"])
        
        elif session["roles"] == "rea":
            return render_template("home.html", role="Real Estate Agent")
        elif session["roles"] == "buyer":
            return render_template("home.html", role=session["roles"])
        elif session["roles"] == "seller":
            return render_template("home.html", role=session["roles"])
        return False  
    else:
        return redirect('/')