from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.User.userProfileController import UserProfileController
from testdatabase import db, collection

userProfile = Blueprint('userProfile', __name__)

@userProfile.route('/userProfile', methods = ['GET'])
def displayProfile():
    if request.method == "GET":
        if "user_email" in session:
            user = UserProfileController.displayUserProfile('user_email')
            return render_template('userProfile.html', user=user)
    
            
    
    