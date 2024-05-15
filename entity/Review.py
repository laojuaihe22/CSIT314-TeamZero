from pymongo import MongoClient

class Review:
    
    def __init__(self):
        self.database = None
        
        
    def get_database(self):
        if self.database is None:
            # Establish a connection to the MongoDB server
            self.database = MongoClient("mongodb+srv://mongo:mongo@cluster0.zj42wez.mongodb.net/")
            
        return self.database
    
    
    def viewReviewByagentEmail(self,email):
        client = self.get_database()
        db = client["CSIT314"]
        
        agent = db.UserAccount.find_one({"email":email})
        
        if agent:
            review_list = list(db.Review.find({"receiver_id":agent["_id"]}))
            
            if review_list:
                return review_list
            else:
                return False;