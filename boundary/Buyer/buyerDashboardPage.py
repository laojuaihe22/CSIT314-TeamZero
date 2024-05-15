from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash

buyer_dashboard_app = Blueprint('buyer_dashboard_app', __name__)

@buyer_dashboard_app.route('/buyer_dashboard', methods=['GET'])
def buyer_dashboard_page():
    
    if "user_email" in session:
        return render_template('buyerDashboard.html')
    else:
        return redirect(url_for('login_app.displayHomePage'))