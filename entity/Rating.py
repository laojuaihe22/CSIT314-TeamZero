from pymongo import MongoClient

class Rating:
    
    def __init__(self):
        self.database = None
        
        
    def get_database(self):
        if self.database is None:
            # Establish a connection to the MongoDB server
            self.database = MongoClient("mongodb+srv://mongo:mongo@cluster0.zj42wez.mongodb.net/")
            # self.database = MongoClient("mongodb://localhost:27017")
        return self.database
    
    
    def viewRatingByagentEmail(self,email):
        client = self.get_database()
        db = client["CSIT314"]
        
        agent = db.UserAccount.find_one({"email":email})
        
        if agent:
            rating_list = list(db.Rating.find({"receiver_id":agent["_id"]}))
            
            if rating_list:
                return rating_list
            else:
                return False;
        