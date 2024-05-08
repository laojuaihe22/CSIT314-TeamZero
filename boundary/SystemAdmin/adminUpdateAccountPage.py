from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.SystemAdmin.updateUserAccountController import UpdateUserAccountController

update_account_app = Blueprint('update_account_app', __name__)


@update_account_app.route('/updateUserAccount', methods=['GET', 'POST'])
def update_profile_page():

    if request.method == "POST":
        user_email = request.form["email"]
        field = request.form["field"]
        value = request.form["value"]
        
        updateUserAccountController = UpdateUserAccountController()
        updateUser = updateUserAccountController.updateUserAccount(user_email, field, value)

        if updateUser:
            flash(f'User Profile updated ', 'success')
            return redirect(url_for('login_app.displayLoginPage'))
        else:
            flash('Email doesn\'t exists', 'error')
        
    return render_template('admin.html')