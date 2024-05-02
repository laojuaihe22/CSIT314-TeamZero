from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.SystemAdmin.viewUserAccountController import ViewUserAccountController

view_account_app = Blueprint('view_account_app', __name__)

@view_account_app.route('/viewUserAccount', methods=['GET', 'POST'])
def view_account():
    
    if request.method == "POST":
        viewUserAccountController = ViewUserAccountController()
        user_account_data = viewUserAccountController.getUserAccountData()
        return render_template('admin.html',users=user_account_data,email=session['user_email'])
    
    return redirect('/home')