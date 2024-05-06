from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.SystemAdmin.createUserAccountController import CreateUserController

create_account_app = Blueprint('create_account_app', __name__)


@create_account_app.route('/createUserAccount', methods=['GET', 'POST'])
def create_account_page():
    
    if request.method == "POST":
        user_email = request.form["email"]
        user_pass = request.form["password"]
        user_role = request.form.get('role')
        createUserController = CreateUserController()
        is_created = createUserController.createUserAccount(user_email,user_pass,user_role)
        
        if is_created:
            flash(f'{session["user_email"]} you have create the account!', 'success')
        else:
            flash('Email existed please enter another email!', 'error')
        
    return redirect('/home')