from flask import Flask
from boundary.User.userLoginPage import login_app
from boundary.User.userLogoutPage import logout_app
from boundary.SystemAdmin.adminCreateAccountPage import create_account_app
from boundary.SystemAdmin.adminSuspendAccountPage import suspend_account_app
from boundary.SystemAdmin.adminViewAccountPage import view_account_app
from boundary.SystemAdmin.adminSearchAccountPage import search_account_app
from boundary.SystemAdmin.adminUpdateAccountPage import update_account_app
from boundary.SystemAdmin.adminCreateProfilePage import create_profile_app
from boundary.SystemAdmin.adminViewUserProfilePage import view_profile_app
from boundary.SystemAdmin.adminSuspendProfilePage import suspend_profile_app
from boundary.SystemAdmin.adminSearchProfilePage import search_profile_app
from boundary.SystemAdmin.adminUpdateProfilePage import update_profile_app
from boundary.RealEstateAgent.agentCreatePropertyListingPage import create_property_listing_app
from boundary.RealEstateAgent.agentViewPropertyListingPage import view_property_listing_app
from boundary.RealEstateAgent.agentUpdatePropertyListingPage import update_property_listing_app
from boundary.RealEstateAgent.agentDeletePropertyListingPage import delete_property_listing_app
from boundary.RealEstateAgent.agentSearchPropertyListingPage import search_property_listing_app
from boundary.RealEstateAgent.agentDashboardPage import rea_dashboard_app

from datetime import timedelta

app = Flask(__name__)
app.secret_key = "123"
app.permanent_session_lifetime = timedelta(hours=1)

# blueprint for loginPage
app.register_blueprint(login_app)
app.register_blueprint(logout_app)
app.register_blueprint(create_account_app)
app.register_blueprint(suspend_account_app)
app.register_blueprint(update_account_app)
app.register_blueprint(view_account_app)
app.register_blueprint(search_account_app)
app.register_blueprint(create_profile_app)
app.register_blueprint(view_profile_app)
app.register_blueprint(suspend_profile_app)
app.register_blueprint(search_profile_app)
app.register_blueprint(update_profile_app)
app.register_blueprint(create_property_listing_app)
app.register_blueprint(view_property_listing_app)
app.register_blueprint(update_property_listing_app)
app.register_blueprint(delete_property_listing_app)
app.register_blueprint(search_property_listing_app)
app.register_blueprint(rea_dashboard_app)

# Run the Flask application
if __name__ == "__main__":  
    app.run(debug=True)