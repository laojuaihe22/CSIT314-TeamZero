from pymongo import MongoClient

class User:
    def __init__(self):
        self.database = None
    def get_database(self):
        if self.database is None:
            # Establish a connection to the MongoDB server
            self.database = MongoClient("mongodb://localhost:27017/")
        return self.database
    
    #61 As a system admin, I want to log in to the management system, so that I can perform administrative tasks and manage the system effectively.
    #63 As a real estate agent, I want to be able to log in to the real estate platform using my email address and password.
    #89 As a buyers, I want to be able to log in to the real estate platform using my email address and password.
    #91 As a sellers, I want to be able to log in to the real estate platform using my email address and password.
    def verifyAccount(self,email,password):
        # Get the MongoDB client
        client = self.get_database()

        # Access a specific database
        db = client["CSIT314"]

        # Access a specific collection within the database
        collection = db["User"]

        # Now you can perform database operations using the collection object
        user = collection.find_one({"email": email, "password": password})
        
        if user:
            return True, user.get('role')
        else:
            return False, "None"
    
    def createUserAccount(self,email, password, role):
        
        # Get the MongoDB client
        client = self.get_database()
        
        # Access a specific database
        db = client["CSIT314"]
        
        # Access a specific collection within the database
        collection = db["User"]
        
        try:
            # Check if email already exists in the database
            existing_user = collection.find_one({'email': email})
            
            if existing_user:
                return False
            
            user_data = {
                "email": email,
                "password": password,
                "role": role
            }
            
            # Insert user data into the database
            collection.insert_one(user_data)
            return True
        
        except Exception as e:
            # Log the exception or return an error message
            return False
        
    def deleteUserAccount(self, email):
        # Get the MongoDB client
        client = self.get_database()
        
        # Access a specific database
        db = client["CSIT314"]
        
        # Access a specific collection within the database
        collection = db["User"]
        
        user = collection.find_one({"email": email})    
        
        if user:
            # Delete the document
            collection.delete_one({"email": email})
            return True
        else:
            return False
        
    def getUserAccountData(self):
        # Get the MongoDB client
        client = self.get_database()
        
        # Access a specific database
        db = client["CSIT314"]
        
        # Access a specific collection within the database
        collection = db["User"]
        
        user_account_data = list(collection.find())
        
        return user_account_data
        
    def getUserAccount(self,email):
    
        client = self.get_database()
        db = client["CSIT314"]
        collection = db["User"]
        
        user = collection.find_one({"email": email})  
        
        if user:
            return user
        else :
            return False 
        