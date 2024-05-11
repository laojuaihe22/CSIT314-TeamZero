from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.SystemAdmin.searchUserAccountController import SearchUserAccountController

search_account_app = Blueprint('search_account_app', __name__)

@search_account_app.route('/searchUserAccount', methods=['GET', 'POST'])
def search_account():

    if request.method == "POST":
        user_email = request.form["email"]
        searchUserAccountController = SearchUserAccountController()
        user_account_data = searchUserAccountController.searchUserAccount(user_email)
        
        if user_account_data:
            return render_template('adminSearchUserAccount.html',user=user_account_data)
        else:
            return render_template('adminSearchUserAccount.html',message='Invalid email!')
            
            
    return render_template('adminSearchUserAccount.html')
