from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from website.mydb import users #import database
from flask_login import login_user, login_required, logout_user, current_user
from .loginController.loginController import LoginController



auth = Blueprint('auth', __name__)
views = Blueprint('views', __name__)

@views.route('/', methods = ['GET', 'POST'])
# @login_required()
def home():
    # if request.method == 'POST':
    #    pass
   
    return render_template("index.html")
    

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if LoginController.verifyAccount(email, password, users):
            flash('Logged in successfully!', category='success')
            return redirect(url_for('auth.home'))
        else:
            flash('Incorrect email or password, please try again.', category='error')

    return render_template("index.html", user=current_user)

@auth.route('/logout',methods = ['GET', 'POST'])
# @login_required
def logout():
    logout_user()
    return render_template()   


@auth.route('/home',methods = ['GET', 'POST'])
# @login_required
def home():
    
    return render_template("home.html", user = current_user) 


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        password_re = request.form.get('password_re')

        user = users.find_one({"email": email})
        
        if user:
            flash('Email already exists, please use another email', category='error')
        elif len(password) < 3:
            flash('Password must be greater than 3 characters', category='error')
        elif password != password_re:
            flash('Passwords don\'t match', category='error')
        else:
            hashed_password = generate_password_hash(password, method='pbkdf2')
            new_user = User(email=email, password=hashed_password)
            users.insert_one({"email": email, "password": hashed_password})
            # login_user(new_user, remember=True)
            flash('Account created successfully!!', category='success')
            return redirect(url_for("auth.login"))
        
        
    return render_template("signUpPage.html", user=current_user)
