from pymongo import MongoClient
from bson import ObjectId
class Review:
    
    def __init__(self):
        self.database = None
        
        
    def get_database(self):
        if self.database is None:
            # Establish a connection to the MongoDB server
            # self.database = MongoClient("mongodb://localhost:27017")
            self.database = MongoClient("mongodb+srv://mongo:mongo@cluster0.zj42wez.mongodb.net/")
            
        return self.database
    
    #195 As a real estate agent, I want to view reviews of myself, so that I can understand my clients' feedback and improve my services accordingly.
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

    #261 As a buyer, I want to write a review of my experience working with a real estate agent so that other users can learn more about their services
    #324 As a seller, I want to write a review of my experience working with a real estate agent so that other users can learn more about their services
    def submitReview(self,agent_email, sender_id, review):
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
                    "review": review
                })
            if submit_review:
                return True
            else:
                return False
