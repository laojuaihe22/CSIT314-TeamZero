from flask import Flask
from boundary.User.userLoginPage import login_app
from boundary.User.userLogoutPage import logout_app
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "123"
app.permanent_session_lifetime = timedelta(minutes=5)

# blueprint for loginPage
app.register_blueprint(login_app)
app.register_blueprint(logout_app)



# Run the Flask application
if __name__ == "__main__":  
    app.run(debug=True)