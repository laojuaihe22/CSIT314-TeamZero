from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.SystemAdmin.createUserProfileController import CreateUserProfileController
from controller.SystemAdmin.viewUserAccountController import ViewUserAccountController


create_profile_app = Blueprint('create_profile_app', __name__)


@create_profile_app.route('/createUserProfile', methods=['GET', 'POST'])
def create_profile_page():
    
    if request.method == "POST":
        user_email = request.form["email"]
        user_name = request.form["name"]
        user_description = request.form["description"]

        createUserProfileController = CreateUserProfileController()
        is_created = createUserProfileController.createUserProfile(user_email, user_name, user_description)

        if is_created:
            flash(f'Profile created successfully', 'success')
        else:
            flash('Email doesn\'t exists', 'error')


    viewUserAccountController = ViewUserAccountController()
    user_account_data = viewUserAccountController.viewUserAccountData()
    return render_template('adminCreateProfile.html', users = user_account_data)