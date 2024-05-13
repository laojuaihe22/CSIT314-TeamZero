from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash

rea_dashboard_app = Blueprint('rea_dashboard_app', __name__)

@rea_dashboard_app.route('/rea_dashboard', methods=['GET'])
def rea_dashboard_page():
    
    if "user_email" in session:
        return render_template('realEstateAgentDashboard.html')
    else:
        return redirect(url_for('login_app.displayHomePage'))