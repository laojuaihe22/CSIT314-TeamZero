from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.User.userProfileController import UserProfileController
from flask import jsonify
userProfile = Blueprint('userProfile', __name__)

@userProfile.route('/userProfile', methods = ['GET'])
def displayProfile():
    if request.method == "GET":
        if "user_email" in session:
            user_profile_controller = UserProfileController()
            user = user_profile_controller.viewUserProfile(session["user_email"])
            
            return render_template('userProfile.html', user=user)
