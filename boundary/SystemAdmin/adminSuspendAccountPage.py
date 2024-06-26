from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.SystemAdmin.suspendUserAccountController import SuspendUserAccountController


suspend_account_app = Blueprint('suspend_account_app', __name__)


@suspend_account_app.route('/suspendUserAccount', methods=['POST','GET'])
def suspend_account_page():
    
    if request.method == "POST":
        user_email = request.form["email"]
        user_email_retype = request.form["email_re"]
        
        if user_email != user_email_retype:
            return render_template('adminSuspendAccount.html',message='Email mismatch!')
        

        suspendUserController = SuspendUserAccountController()
        is_suspend = suspendUserController.suspendUserAccount(user_email)
        
        if is_suspend:
            return render_template('adminSuspendAccount.html',message='Account successfully suspended!')
        else:
            return render_template('adminSuspendAccount.html',message='Email not existed please enter again')
        
    return render_template('adminSuspendAccount.html')