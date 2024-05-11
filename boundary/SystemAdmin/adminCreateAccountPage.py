from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.SystemAdmin.createUserAccountController import CreateUserAccountController

create_account_app = Blueprint('create_account_app', __name__)


@create_account_app.route('/createUserAccount', methods=['POST','GET'])
def create_account_page():
    
    if request.method == "POST":
        user_email = request.form["email"]
        user_pass = request.form["password"]
        user_role = request.form.get('role')
        createUserController = CreateUserAccountController()
        is_created = createUserController.createUserAccount(user_email,user_pass,user_role)
        
        if is_created:
            return render_template('adminCreateAccount.html',message='Account created successfully!')
        else:
            return render_template('adminCreateAccount.html',message='This email is already registered!')
        
    return render_template('adminCreateAccount.html')

@create_account_app.route('/userAccount', methods=['GET'])
def user_account():
    if "user_email" in session:
        return render_template('userAccount.html')
    

@create_account_app.route('/userProfile', methods=['GET'])
def user_profile():
    if "user_email" in session:
        return render_template('userHomeProfile.html')