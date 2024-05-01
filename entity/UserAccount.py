from pymongo import MongoClient

class User:
    def __init__(self):
        self.database = None
        self.role = ""
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
            self.role = user.get('role')
            return True
        else:
            False;
    
    def getUserRole(self):
        return self.role    