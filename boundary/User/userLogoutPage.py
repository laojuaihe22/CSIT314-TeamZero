from flask import redirect, session, Blueprint

logout_app = Blueprint('logout_app', __name__)

@logout_app.route("/logout", methods=["POST", "GET"])
def displayLogoutPage():
    session.clear()
    return redirect('/')  # Redirect to login page after logout
