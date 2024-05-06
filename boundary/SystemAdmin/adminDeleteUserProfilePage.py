from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.SystemAdmin.deleteUserProfileController import DeleteUserProfile

delete_profile_app = Blueprint('delete_profile_app', __name__)

@delete_profile_app.route('/deleteUserProfilePage', methods=['GET', 'POST'])
def delete_profile_page():
    return render_template('deleteProfile.html')

@delete_profile_app.route('/deleteUserProfile', methods=['GET', 'POST'])
def delete_profile():
    if request.method == "POST":
        user_email = request.form["email"]

        deleteUserProfile = DeleteUserProfile()
        is_deleted = deleteUserProfile.deleteUserProfile(user_email)

        if is_deleted:
            flash(f'{session["user_email"]}\'s profile deleted!', 'success')
        else:
            flash('Email doesn\'t exists, please enter again', 'error')
        
    return redirect('/home')