from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.SystemAdmin.createUserProfileController import CreateUserProfileController

create_profile_app = Blueprint('create_profile_app', __name__)


@create_profile_app.route('/createUserProfilePage', methods=['GET', 'POST'])
def create_profile_page():
    return render_template('createUserProfile.html')


@create_profile_app.route('/createUserProfile', methods=['GET', 'POST'])
def create_profile():
    
    if request.method == "POST":
        user_email = request.form["email"]
        user_name = request.form["name"]
        user_age = request.form["age"]
        user_description = request.form["description"]

        createUserProfileController = CreateUserProfileController()
        is_created = createUserProfileController.createUserProfile(user_email, user_name, user_age, user_description)

        if is_created:
            flash(f'Profile created for {session["user_email"]}', 'success')
        else:
            flash('Email doesn\'t exists', 'error')
        
    return redirect(url_for('create_profile_app.create_profile_page'))