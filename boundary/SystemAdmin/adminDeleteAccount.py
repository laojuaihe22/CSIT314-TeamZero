from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.SystemAdmin.deleteUserAccount import DeleteUserAccount

delete_account_app = Blueprint('delete_account_app', __name__)


@delete_account_app.route('/deleteUserAccount', methods=['GET', 'POST'])
def delete_account():
    
    if request.method == "POST":
        user_email = request.form["email"]

        deleteUserController = DeleteUserAccount()
        is_deleted = deleteUserController.deleteUserAccount(user_email)
        
        if is_deleted:
            flash(f'{session["user_email"]} you have delete the account!', category='success')
        else:
            flash('something have went wrong', 'error')
        
    return render_template('adminDeleteUserAccount.html', email=session["user_email"])