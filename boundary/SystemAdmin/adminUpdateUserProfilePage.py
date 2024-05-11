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
        
        updateUserProfileController = UpdateUserProfileController()
        updateUser = updateUserProfileController.updateUserProfile(user_email, field, value)

        if updateUser:
            flash(f'{user_email}\'s user profile updated!', 'success')
            return render_template('/adminUpdateProfile.html', updateUser=updateUser)
        else:
            flash('No profile has been updated', 'error')
            return render_template('/adminUpdateProfile.html', updateUser=None)
    
    viewUserAccountController = ViewUserAccountController()
    user_account_data = viewUserAccountController.viewUserAccountData()
    return render_template('/adminUpdateProfile.html', users = user_account_data)