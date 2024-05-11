from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.SystemAdmin.viewUserProfileController import ViewUserProfileController

view_profile_app = Blueprint('view_profile_app', __name__)

@view_profile_app.route('/viewUserProfile', methods=['GET', 'POST'])
def view_profile_page():

    if request.method == "GET":
        viewUserProfileController = ViewUserProfileController()
        user_profile_data = viewUserProfileController.viewUserProfile()
        return render_template('adminViewProfile.html',users=user_profile_data)
    
    return redirect('/home')