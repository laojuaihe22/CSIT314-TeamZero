from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.SystemAdmin.updateUserProfileController import UpdateUserProfileController
from controller.SystemAdmin.viewUserAccountController import ViewUserAccountController

update_profile_app = Blueprint('update_profile_app', __name__)

@update_profile_app.route('/updateUserProfile', methods=['GET', 'POST'])
def update_profile_page():

    if request.method == "POST":

        user_email = request.form["email"]
        field = request.form["field"]
        value = request.form["value"]
        
        # Validate email format
        if field == "email" and not is_valid_email(value):
            return render_template('adminUpdateAccount.html', message="Update Value is Invalid email format! Please try again")
        
        if field == "status":
            # Check if the value is a boolean
            if value.lower() == "true":
                value = True
            elif value.lower() == "false":
                value = False
            else:
                flash('Status field requires a boolean value (True or False)', 'error')
                return render_template('/adminUpdateProfile.html')

        updateUserProfileController = UpdateUserProfileController()
        updateUser = updateUserProfileController.updateUserProfile(user_email, field, value)

        if updateUser:
            return render_template('/adminUpdateProfile.html', message = 'User profile updated!')
        else:
            
            return render_template('/adminUpdateProfile.html', message = 'No profile has been updated')
    
    
    return render_template('/adminUpdateProfile.html')


def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None