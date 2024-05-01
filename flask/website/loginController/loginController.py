from website.models import User
from website.mydb import users
from werkzeug.security import generate_password_hash, check_password_hash

class LoginController:

   def verifyAccount(email, password, users):
        user = users.find_one({"email": email})
        if user and check_password_hash(user.get('password'), password):
            return True
        else:
            return False