from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.SystemAdmin.updateUserAccountController import UpdateUserAccountController
import re

update_account_app = Blueprint('update_account_app', __name__)


@update_account_app.route('/updateUserAccount', methods=['GET', 'POST'])
def update_profile_page():

    if request.method == "POST":
        user_email = request.form["email"]
        field = request.form["field"]
        value = request.form["value"]
        
        # Validate email format
        if field == "email" and not is_valid_email(value):
            return render_template('adminUpdateAccount.html', message="Update Value is Invalid email format! Please try again")
        
        if field == "status":
            # Convert value to boolean if field is status
            if value.lower() == "true":
                value = True
            elif value.lower() == "false":
                value = False
            else:
                return render_template('adminUpdateAccount.html', message="Status can only be 'true' or 'false'")
        
        
        updateUserAccountController = UpdateUserAccountController()
        updateUser = updateUserAccountController.updateUserAccount(user_email, field, value)

        if updateUser:
            return render_template('adminUpdateAccount.html',message="User Profile updated !")
        else:
            return render_template('adminUpdateAccount.html',message="Email doesn\'t exists ")
        
    return render_template('adminUpdateAccount.html')

def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None