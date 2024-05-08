from flask import Blueprint, redirect, render_template, request, session, flash, url_for
from controller.User.signUpController import SignUpController


signUp_app = Blueprint('signUp_app', __name__)

@signUp_app.route("/sign-up", methods=["POST","GET"])
def signUpPage():
    
    if request.method == "POST":
        sign_up_email = request.form["email"]
        sign_up_password = request.form["password"]
        
        signUpController = SignUpController()
        is_created = signUpController.signUpUser(sign_up_email, sign_up_password)
        
        if is_created:
            flash('Account created successfully!!', category='success')
            return redirect('/')
        else:
            flash('Email already exists, please use another email', category='error')
            return redirect(url_for('signUp_app.signUpPage'))
    else:
        return render_template('signUpPage.html')