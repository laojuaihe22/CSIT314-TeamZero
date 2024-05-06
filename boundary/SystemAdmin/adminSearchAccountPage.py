from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.SystemAdmin.searchUserAccountController import SearchUserAccountController

search_account_app = Blueprint('search_account_app', __name__)

@search_account_app.route('/searchUserAccount', methods=['GET', 'POST'])
def view_account_page():
    
    if request.method == "POST":
        user_email = request.form["email"]
        searchUserAccountController = SearchUserAccountController()
        user_account_data = searchUserAccountController.searchUserAccount(user_email)
        
        if user_account_data:
            return render_template('admin.html',searchUser=user_account_data,email=session['user_email'])
        else:
            flash('Invalid email', 'error')
    return redirect('/home')