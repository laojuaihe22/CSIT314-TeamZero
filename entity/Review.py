from pymongo import MongoClient
from bson import ObjectId
class Review:
    
    def __init__(self):
        self.database = None
        
        
    def get_database(self):
        if self.database is None:
            # Establish a connection to the MongoDB server
            self.database = MongoClient("mongodb://localhost:27017")
            
        return self.database
    
    
    def viewReviewByagentId(self,agentId):
        client = self.get_database()
        db = client["CSIT314"]
        
        agent = db.UserAccount.find_one({"_id":ObjectId(agentId)})
        
        if agent:
            review_list = list(db.Review.find({"receiver_id":ObjectId(agentId)}))
            
            if review_list:
                return review_list
            else:
                return False;