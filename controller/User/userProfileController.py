from flask import session
from entity.UserAccount import User
from testdatabase import db, collection
from entity.UserAccount import User

class UserProfileController:
    
    def displayUserProfile(self):
        dbManager = User()
        client = dbManager.get_database()
        db = client["CSIT314"]
        collection = db["User"]
        user_email = session.get('user_email')
        userObj = collection.find_one({"email": user_email})
        return userObj
    