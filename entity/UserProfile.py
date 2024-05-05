from pymongo import MongoClient

class UserProfile:
    def __init__(self):
        self.database = None
        
        
    def get_database(self):
        if self.database is None:
            # Establish a connection to the MongoDB server
            self.database = MongoClient("mongodb+srv://mongo:mongo@cluster0.zj42wez.mongodb.net/")
        return self.database
    
    
    # view user profile
    def displayUserProfile(self, email):
        
        client = self.get_database()
        
        db = client["CSIT314"]
        collection = db["User"]
        
        userObj = collection.find_one({"email": email})
        
        return userObj