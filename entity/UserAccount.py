from pymongo import MongoClient

class UserAccount:
    def __init__(self):
        self.database = None
    def get_database(self):
        if self.database is None:
            # Establish a connection to the MongoDB server
            # self.database = MongoClient("mongodb+srv://mongo:mongo@cluster0.zj42wez.mongodb.net/?tls=true")
            self.database = MongoClient("mongodb://localhost:27017")
            
        return self.database
    
    #61 As a system admin, I want to log in to the management system, so that I can perform administrative tasks and manage the system effectively.
    #63 As a real estate agent, I want to log in to the real estate platform using my email address and password.
    #89 As a buyers, I want to log in to the real estate platform using my email address and password.
    #91 As a sellers, I want to log in to the real estate platform using my email address and password.
    def verifyAccount(self,email,password):

        client = self.get_database()
        db = client["CSIT314"]

        # Find the user account by email
        user_account = db.UserAccount.find_one({'email': email})
        
        if user_account and password == user_account['password'] and user_account["status"]:
            # User is verified, now fetch the user's profile
            user_profile = db.UserProfile.find_one({'userAccountId': user_account['_id']})
            if user_profile:
                return True, user_profile['role'], str(user_account['_id'])
        
        # If verification fails
        return False, "None", "None"
    
    
    #117 As a system admin, I want to create user accounts so that I can grant access to the system to new users.
    def createUserAccount(self,user_email,user_pass,role):
        client = self.get_database()
        db = client["CSIT314"]

        # Check if email already exists in the database
        existing_user = db.UserAccount.find_one({'email': user_email})
        
        if not existing_user:
            

            user_data = {
                "email": user_email,
                "password": user_pass,
                "status": True
            }
            # Insert user data into the UserAccount collection
            user_account_result = db.UserAccount.insert_one(user_data)
            
            # Create user profile with role and reference to the user account

            user_profile_role = {
                "userAccountId": user_account_result.inserted_id,
                "name":"None",
                "role": role,
                "description":"None",
                "status":True
            }
            
            db.UserProfile.insert_one(user_profile_role)
            

            return True
        else:
            return False
        

        
    #120 As a system admin, I want to suspend user accounts so that I can revoke access to the system for users who no longer need it
    def suspendUserAccount(self, user_email):

        client = self.get_database()
        db = client["CSIT314"]
        
        user = db.UserAccount.find_one({"email": user_email})    
        
        if user:
            db.UserAccount.update_one(
                {"email": user_email},
                {"$set": {"status": False}}
            )
            return True
        else:
            return False

    #119 As a system admin, I want to update user accounts so that users can change their email and password as needed
    def updateUserAccount(self, user_email, field, value):
        
        client = self.get_database()
        db = client["CSIT314"]
        
        user = db.UserAccount.find_one({"email": user_email}) 
        
        if user:
            db.UserAccount.update_one(
                {"email": user_email},
                {"$set": {field: value}}
            )
            
            return True
        else:
            return False
        
    #118 As a system admin, I want to view basic information of user accounts, so that I can quickly identify users.    
    def viewUserAccountData(self):

        client = self.get_database()
        db = client["CSIT314"]
        
        user_account_data = list(db.UserAccount.find())
        
        return user_account_data
        
        
    #121 As a system admin, I want to search for user accounts so that I can perform administrative tasks for specific users.
    def searchUserAccount(self,email):
    
        client = self.get_database()
        db = client["CSIT314"]
        collection = db["UserAccount"]


        user = collection.find_one({"email": email})  
        
        if user:
            return user
        else :
            return False 
    