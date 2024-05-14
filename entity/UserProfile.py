from pymongo import MongoClient

class UserProfile:
    def __init__(self):
        self.database = None
        
        
    def get_database(self):
        if self.database is None:
            # Establish a connection to the MongoDB server
            self.database = MongoClient("mongodb://localhost:27017")
        return self.database
    

    
    #create user profile
    def createUserProfile(self, user_email, user_name, user_description):
        
        client = self.get_database()
        
        db = client["CSIT314"]
        collection = db["User"]

        try:
            # Check if email exists in the database
            existing_user = collection.find_one({'email': user_email})
            
            if existing_user:
                updated_user_data = {
                    "$set": {
                        "profile.name": user_name,
                        "profile.description": user_description,
                        }
                    }
                
                collection.update_one({"email": user_email}, updated_user_data)
                return True
        
        except Exception as e:
            # Log the exception or return an error message
            return False
    
    #view userr profiles
    def adminViewUserProfile(self):

        client = self.get_database()
        
        db = client["CSIT314"]
        collection = db["User"]

        user_profile_data = list(collection.find())
        
        return user_profile_data

    # suspend user profiles
    def suspendUserProfile(self, user_email):

        client = self.get_database()
        
        db = client["CSIT314"]
        collection = db["User"]

        user = collection.find_one({"email": user_email})    
        
        if user:
            # suspend profile
            collection.update_one({"email": user_email}, {"$set":{"status": False}})
            return True
        else:
            return False
        
    #search user profile
    def searchUserProfile(self, user_email):

        client = self.get_database()
        
        db = client["CSIT314"]
        collection = db["User"]

        userObj = collection.find_one({"email": user_email})
        return userObj
    
    #update user profile
    def updateUserProfile(self, email, field, value):
        
        client = self.get_database()
        db = client["CSIT314"]
        collection = db["User"]

        user = collection.find_one({"email": email})  

        if user:
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

            collection.update_one({"email": email}, update_query)
            updated_user = collection.find_one({'email': email})
            return updated_user
        else:
            return None
