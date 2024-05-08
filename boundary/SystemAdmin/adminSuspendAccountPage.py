from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.SystemAdmin.deleteUserAccountController import SuspendUserAccount

delete_account_app = Blueprint('delete_account_app', __name__)


@delete_account_app.route('/suspendUserAccount', methods=['POST'])
def delete_account_page():
    
    if request.method == "POST":
        user_email = request.form["email"]

        deleteUserController = SuspendUserAccount()
        is_deleted = deleteUserController.suspendUserAccount(user_email)
        
        if is_deleted:
            flash(f'{session["user_email"]} you have suspend the account!', 'success')
        else:
            flash('Email not existed please enter again', 'error')
        
    return redirect('/home')