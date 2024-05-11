from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.SystemAdmin.searchUserProfileController import SearchUserProfileController
from controller.SystemAdmin.viewUserAccountController import ViewUserAccountController

search_profile_app = Blueprint('search_profile_app', __name__)



@search_profile_app.route('/searchUserProfile', methods=['GET', 'POST'])
def search_profile_page():
    if request.method == "POST":
        user_email = request.form.get("email")  # Use request.form.get to safely retrieve form data
        searchUserProfileController = SearchUserProfileController()
        user_account_data = searchUserProfileController.searchUserProfile(user_email)
        
        if user_account_data:
            return render_template('adminSearchProfile.html', searchUser=user_account_data)
        else:

            return render_template('adminSearchProfile.html', searchUser= None)
    
    viewUserAccountController = ViewUserAccountController()
    user_account_data = viewUserAccountController.viewUserAccountData()
    return render_template('adminSearchProfile.html', users = user_account_data)