from pymongo import MongoClient

class UserProfile:
    def __init__(self):
        self.database = None
        
        
    def get_database(self):
        if self.database is None:
            # Establish a connection to the MongoDB server
            # self.database = MongoClient("mongodb+srv://mongo:mongo@cluster0.zj42wez.mongodb.net/")
            self.database = MongoClient("mongodb://localhost:27017")
            
        return self.database
    
    
    #122 As a system admin, I want to create user profile so that I can grant access to the system to new users.
    def createUserProfile(self, user_email, user_name, user_description):
        
        client = self.get_database()
        
        db = client["CSIT314"]


        # Check if email exists in the database
        existing_user = db.UserAccount.find_one({'email': user_email})
        
        if existing_user:
            updated_user_data = {
                "$set": {
                    "name": user_name,
                    "status": True,
                    "description": user_description,
                    }
                }
            
            db.UserProfile.update_one({"userAccountId": existing_user["_id"]}, updated_user_data)
            return True
    
        else:
            # Log the exception or return an error message
            return False
    
    #123 As a system admin, I want to view basic information of user profile, So that I can quickly identify users
    def adminViewUserProfile(self):

        client = self.get_database()
        
        db = client["CSIT314"]
        
        pipeline = [
            {
                '$lookup': {
                    'from': 'UserAccount', 
                    'localField': 'userAccountId', 
                    'foreignField': '_id', 
                    'as': 'result'
                }
            }, {
                '$unwind': {
                    'path': '$result'
                }
            }
        ]

        user_profile_data = list(db.UserProfile.aggregate(pipeline))
        
        return user_profile_data

    # 125 As a system admin, I want to suspend user profile so that I can revoke access to the system for users who no longer need it.
    def suspendUserProfile(self, user_email):

        client = self.get_database()
        
        db = client["CSIT314"]

        user = db.UserAccount.find_one({"email": user_email})    
        
        if user:
            # suspend profile
            db.UserProfile.update_one({"userAccountId":user["_id"]}, {"$set":{"status": False}})
            return True
        else:
            return False
        
    #126 As a system admin, I want to search user profiles so that I can quickly locate specific users and review their account details.
    def searchUserProfile(self, user_email):

        client = self.get_database()
        
        db = client["CSIT314"]

        user = db.UserAccount.find_one({"email": user_email})
        if user:
            userObj = db.UserProfile.find_one({"userAccountId":user["_id"]})
            if userObj:
                return userObj
            else:
                return False
    
    #124 As a system admin, I want to update user profiles so that I can ensure accurate and up-to-date information.
    def updateUserProfile(self, email, field, value):
        
        client = self.get_database()
        db = client["CSIT314"]
        
        user = db.UserAccount.find_one({"email": email}) 
        
        if user:
            user_profile = db.UserProfile.find_one({"userAccountId":user['_id']})
            if user_profile:
                db.UserProfile.update_one(
                    {'_id':user_profile['_id']},
                    {"$set": {field: value}}
                )
                return True
        else:
            return False
