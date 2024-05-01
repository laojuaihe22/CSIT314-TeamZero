from flask import redirect, session, Blueprint

logout_app = Blueprint('login_controller', __name__)

@logout_app.route("/logout", methods=["POST", "GET"])
def displayLogoutPage():
    session.pop("user_email", None)
    session.pop("password", None)
    session.pop("roles", None)
    return redirect('/')  # Redirect to login page after logout
