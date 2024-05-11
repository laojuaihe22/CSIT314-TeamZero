from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.SystemAdmin.suspendUserProfileController import SuspendUserProfile

suspend_profile_app = Blueprint('suspend_profile_app', __name__)

@suspend_profile_app.route('/suspendUserProfile', methods=['GET', 'POST'])
def suspend_profile_page():
    if request.method == "POST":
        user_email = request.form["email"]

        suspendUserProfile = SuspendUserProfile()
        is_deleted = suspendUserProfile.suspendUserProfile(user_email)

        if is_deleted:
            flash(f'{session["user_email"]}\'s profile suspended!', 'success')
        else:
            flash('Email doesn\'t exists, please enter again', 'error')
        
    return render_template('suspendProfile.html')