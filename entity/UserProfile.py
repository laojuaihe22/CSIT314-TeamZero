from pymongo import MongoClient

class UserProfile:
    def __init__(self):
        self.database = None
        
        
    def get_database(self):
        if self.database is None:
            # Establish a connection to the MongoDB server
            self.database = MongoClient("mongodb://localhost:27017/")
        return self.database
    
    
    # view user profile
    def viewUserProfile(self, email):
        
        client = self.get_database()
        
        db = client["CSIT314"]
        collection = db["User"]
        
        userObj = collection.find_one({"email": email})
        
        return userObj

    
    #create user profile
    def createUserProfile(self, email, name, age, description):
        
        client = self.get_database()
        
        db = client["CSIT314"]
        collection = db["User"]

        try:
            # Check if email exists in the database
            existing_user = collection.find_one({'email': email})
            
            if existing_user:
                updated_user_data = {
                    "$set": {
                        "profile": {
                            "name": name,
                            "age": age,
                            "description": description
                        }
                    }
                }
            
                collection.update_one({"email": email}, updated_user_data)
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

    # delete user profiles
    def deleteUserProfile(self, email):

        client = self.get_database()
        
        db = client["CSIT314"]
        collection = db["User"]

        user = collection.find_one({"email": email})    
        
        if user:
            # Delete profile
            collection.update_one({"email": email}, {"$unset": {"profile": ""}})
            return True
        else:
            return False
        
    #search user profile
    def searchUserProfile(self, email):

        client = self.get_database()
        
        db = client["CSIT314"]
        collection = db["User"]

        userObj = collection.find_one({"email": email})
        return userObj
    
    #update user profile
    def updateUserProfile(self, email, field, value):
        
        client = self.get_database()
        db = client["CSIT314"]
        collection = db["User"]

        user = collection.find_one({"email": email})  

        if user:
            update_query = {"$set": {"profile." + field: value}}
            collection.update_one({"email": email}, update_query)
            return True
        else:
            return False
