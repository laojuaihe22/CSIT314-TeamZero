from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.SystemAdmin.updateUserProfileController import UpdateUserProfileController

update_profile_app = Blueprint('update_profile_app', __name__)

@update_profile_app.route('/updateUserProfilePage', methods=['GET', 'POST'])
def update_profile_page():

    return render_template('updateUserProfile.html')

@update_profile_app.route('/updateUserProfile', methods=['GET', 'POST'])
def update_profile():

    if request.method == "POST":

        user_email = request.form["email"]
        field = request.form["field"]
        value = request.form["value"]
        
        updateUserProfileController = UpdateUserProfileController()
        is_created = updateUserProfileController.updateUserProfile(user_email, field, value)

        if is_created:
            flash(f'Profile updated for {session["user_email"]}', 'success')
        else:
            flash('Email doesn\'t exists', 'error')
        
    return redirect('/home')