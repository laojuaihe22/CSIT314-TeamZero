from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.SystemAdmin.viewUserAccountController import ViewUserAccountController

view_account_app = Blueprint('view_account_app', __name__)

@view_account_app.route('/viewUserAccount', methods=['GET','POST'])
def view_account_page():
    
    if request.method == "GET":
        viewUserAccountController = ViewUserAccountController()
        user_account_data = viewUserAccountController.viewUserAccountData()
        return render_template('adminViewAccount.html',users=user_account_data)
    
    return render_template('adminViewAccount.html')