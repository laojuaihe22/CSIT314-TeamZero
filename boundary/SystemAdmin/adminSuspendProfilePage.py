from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.SystemAdmin.suspendUserProfileController import SuspendUserProfileController


suspend_profile_app = Blueprint('suspend_profile_app', __name__)

@suspend_profile_app.route('/suspendUserProfile', methods=['GET', 'POST'])
def suspend_profile_page():
    if request.method == "POST":
        user_email = request.form["email"]
        user_email_retype = request.form["email_re"]
        
        if user_email != user_email_retype:
            return render_template('adminSuspendAccount.html',message='Email mismatch!')

        suspendUserProfile = SuspendUserProfileController()
        is_suspended = suspendUserProfile.suspendUserProfile(user_email)

        if is_suspended:
            return render_template('adminSuspendProfile.html',msg='User Profile successfully suspended!')
        else:
            return render_template('adminSuspendProfile.html',msg='Email doesn\'t exists, please enter again')
    
    return render_template('adminSuspendProfile.html')