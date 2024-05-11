from pymongo import MongoClient

class UserAccount:
    def __init__(self):
        self.database = None
    def get_database(self):
        if self.database is None:
            # Establish a connection to the MongoDB server
            self.database = MongoClient("mongodb+srv://mongo:mongo@cluster0.zj42wez.mongodb.net/")
        return self.database
    
    #61 As a system admin, I want to log in to the management system, so that I can perform administrative tasks and manage the system effectively.
    #63 As a real estate agent, I want to be able to log in to the real estate platform using my email address and password.
    #89 As a buyers, I want to be able to log in to the real estate platform using my email address and password.
    #91 As a sellers, I want to be able to log in to the real estate platform using my email address and password.
    def verifyAccount(self,email,password):

        client = self.get_database()
        db = client["CSIT314"]
        collection = db["User"]

        # Now you can perform database operations using the collection object
        user = collection.find_one({"email": email})
        
        if not user:
            return False, "None"
        

        if user['password'] == password:
            return True, user['profile']['role']
        else:
            return False, "None"
    
    def createUserAccount(self,email, password, role):
        
        client = self.get_database()
        db = client["CSIT314"]
        collection = db["User"]
        
        try:
            # Check if email already exists in the database
            existing_user = collection.find_one({'email': email})
            
            if existing_user:
                return False
            
            user_data = {
                "email": email,
                "password": password,
                "status":True,
                "profile":{"role":role,
                           "status":True,
                           }
            }
            
            # Insert user data into the database
            collection.insert_one(user_data)
            return True
        
        except Exception as e:
            # Log the exception or return an error message
            return False
        
    def suspendUserAccount(self, user_email):

        client = self.get_database()
        db = client["CSIT314"]
        collection = db["User"]
        
        user = collection.find_one({"email": user_email})    
        
        if user:
            collection.update_one(
                {"email": user_email},
                {"$set": {"status": False}}
            )
            return True
        else:
            return False
        
    def updateUserAccount(self, user_email, field, value):
        
        client = self.get_database()
        db = client["CSIT314"]
        collection = db["User"]
        
        user = collection.find_one({"email": user_email}) 
        
        if user:
            collection.update_one(
                {"email": user_email},
                {"$set": {field: value}}
            )
            
            return True
        else:
            return False
        
    def viewUserAccountData(self):

        client = self.get_database()
        db = client["CSIT314"]
        collection = db["User"]
        
        user_account_data = list(collection.find())
        
        return user_account_data
        
    def searchUserAccount(self,email):
    
        client = self.get_database()
        db = client["CSIT314"]
        collection = db["User"]
        
        user = collection.find_one({"email": email})  
        
        if user:
            return user
        else :
            return False 
    
    def signUpUser(self, email,password):
        client = self.get_database()
        db = client["CSIT314"]
        collection = db["User"]
        try:
            # Check if email already exists in the database
            existing_user = collection.find_one({'email': email})
            
            if existing_user:
                return False
            
            user_data = {
                "email": email,
                "password": password,
                "status": True
            }
            
            # Insert user data into the database
            collection.insert_one(user_data)
            return True
        
        except Exception as e:
            # Log the exception or return an error message
            return False