from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.SystemAdmin.suspendUserProfileController import SuspendUserProfile
from controller.SystemAdmin.viewUserAccountController import ViewUserAccountController

suspend_profile_app = Blueprint('suspend_profile_app', __name__)

@suspend_profile_app.route('/suspendUserProfile', methods=['GET', 'POST'])
def suspend_profile_page():
    if request.method == "POST":
        user_email = request.form["email"]

        suspendUserProfile = SuspendUserProfile()
        is_deleted = suspendUserProfile.suspendUserProfile(user_email)

        if is_deleted:
            flash(f'{user_email}\'s profile suspended!', 'success')
        else:
            flash('Email doesn\'t exists, please enter again', 'error')
    
    viewUserAccountController = ViewUserAccountController()
    user_account_data = viewUserAccountController.viewUserAccountData()
    return render_template('adminSuspendProfile.html', users = user_account_data)