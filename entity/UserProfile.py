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
    

    
    #create user profile
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
            print("jhere")
            db.UserProfile.update_one({"userAccountId": existing_user["_id"]}, updated_user_data)
            return True
    
        else:
            # Log the exception or return an error message
            return False
    
    #view userr profiles
    def adminViewUserProfile(self):

        client = self.get_database()
        
        db = client["CSIT314"]

        user_profile_data = list(db.UserProfile.find())
        
        return user_profile_data

    # suspend user profiles
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
        
    #search user profile
    def searchUserProfile(self, user_email):

        client = self.get_database()
        
        db = client["CSIT314"]
        

        user = db.UserAccount.find_one({"email": user_email})
        userObj = db.UserProfile.find_one({"userAccountId":user["_id"]})
        return userObj
    
    #update user profile
    def updateUserProfile(self, email, field, value):
        
        client = self.get_database()
        db = client["CSIT314"]
        

        user = db.UserAccount.find_one({"email": email})  
        if user:
            userPro = db.UserProfile.find_one({"userAccountId":user["_id"]})
        else:
            return None

        if userPro:
            if field == "role":
                if value in ["buyer", "seller", "real estate agent"]:  # Check if value is one of the allowed roles
                    update_query = {"$set": {"profile." + field: value}}
                else:
                    return None
                    
            elif field == "status":
                if value in ["False", "True"]:  # Check if value is either "False" or "True"
                    update_query = {"$set": {"profile." + field: value}}
                else:
                    return None

            else:
                # Handle the case where the field is not "role" or "status"
                update_query = {"$set": {"profile." + field: value}}

            db.UserProfile.update_one({"userAccountId":user["_id"]}, update_query)
            updated_user = db.UserProfile.find_one({"userAccountId":user["_id"]})
            return updated_user
        else:
            return None
