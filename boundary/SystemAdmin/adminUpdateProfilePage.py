from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.SystemAdmin.updateUserProfileController import UpdateUserProfileController
from controller.SystemAdmin.viewUserAccountController import ViewUserAccountController

update_profile_app = Blueprint('update_profile_app', __name__)

@update_profile_app.route('/updateUserProfile', methods=['GET', 'POST'])
def update_profile_page():

    viewUserAccountController = ViewUserAccountController()
    user_account_data = viewUserAccountController.viewUserAccountData()

    if request.method == "POST":

        user_email = request.form["email"]
        field = request.form["field"]
        value = request.form["value"]
        
        if field == "status":
            # Check if the value is a boolean
            if value.lower() == "true":
                value = True
            elif value.lower() == "false":
                value = False
            else:
                flash('Status field requires a boolean value (True or False)', 'error')
                return render_template('/adminUpdateProfile.html', updateUser=None, users=user_account_data)

        updateUserProfileController = UpdateUserProfileController()
        updateUser = updateUserProfileController.updateUserProfile(user_email, field, value)

        if updateUser:
            
            return render_template('/adminUpdateProfile.html', updateUser=updateUser,  users=user_account_data, message = 'User profile updated!')
        else:
            
            return render_template('/adminUpdateProfile.html', updateUser=None, users=user_account_data, message = 'No profile has been updated')
    
    
    return render_template('/adminUpdateProfile.html', users=user_account_data)
