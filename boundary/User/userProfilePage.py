from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.User.userProfileController import UserProfileController

userProfile = Blueprint('userProfile', __name__)

@userProfile.route('/userProfile', methods = ['GET'])
def displayProfile():
    if request.method == "GET":
        if "user_email" in session:
            user_profile_controller = UserProfileController()
            user = user_profile_controller.displayUserProfile(session["user_email"])
            
            return render_template('userProfile.html', user=user)
    
            
    
    