from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.SystemAdmin.suspendUserAccountController import SuspendUserAccount


suspend_account_app = Blueprint('suspend_account_app', __name__)


@suspend_account_app.route('/suspendUserAccount', methods=['POST'])
def suspend_account_page():
    
    if request.method == "POST":
        user_email = request.form["email"]

        deleteUserController = SuspendUserAccount()
        is_deleted = deleteUserController.suspendUserAccount(user_email)
        
        if is_deleted:
            flash(f'{session["user_email"]} you have suspend the account!', 'success')
        else:
            flash('Email not existed please enter again', 'error')
        
    return redirect('/home')