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

    def submitReview(self,agent_email, sender_id, buyer_rating):
        client = self.get_database()
        db = client["CSIT314"]
        
        agent = db.UserAccount.find_one({"email": agent_email})
            
        if agent:
            agent_id = agent["_id"]
            profile_info = db.UserProfile.find_one({"userAccountId": agent_id})

            if profile_info and profile_info["role"] == "rea":
                submit_review = db.Review.insert_one({
                    "sender_id": ObjectId(sender_id),
                    "receiver_id": agent["_id"],
                    "review": buyer_rating
                })
                if submit_review:
                    return True
                else:
                    return False
