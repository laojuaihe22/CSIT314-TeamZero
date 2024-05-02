from flask import Flask
from boundary.User.userLoginPage import login_app
from boundary.User.userLogoutPage import logout_app
from boundary.SystemAdmin.adminCreateAccount import create_account_app
from boundary.SystemAdmin.adminDeleteAccount import delete_account_app
from boundary.SystemAdmin.adminViewAccount import view_account_app
from boundary.SystemAdmin.adminSearchUserAccount import search_account_app
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "123"
app.permanent_session_lifetime = timedelta(minutes=5)

# blueprint for loginPage
app.register_blueprint(login_app)
app.register_blueprint(logout_app)
app.register_blueprint(create_account_app)
app.register_blueprint(delete_account_app)
app.register_blueprint(view_account_app)
app.register_blueprint(search_account_app)




# Run the Flask application
if __name__ == "__main__":  
    app.run(debug=True)