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
            review_list = list(db.review.find({"receiver_id":ObjectId(agentId)}))
            
            if review_list:
                return review_list
            else:
                return False;

    def submitReview(self, receiver, sender, review):
        client = self.get_database()
        db = client["CSIT314"]
        
        agent = db.UserAccount.find_one({"email": receiver})
            
        if agent:
            
            agent_id = agent["_id"]

            profile_info = db.UserProfile.find_one({"userAccountId": agent_id})

            if profile_info and profile_info["role"] == "rea":

                existing_review = db.review.find_one({
                "sender_id": ObjectId(sender),
                "receiver_id": agent["_id"]
                })

                if existing_review:
                # If a review already exists, return False indicating that the review cannot be submitted again
                    return False
                else:
                    submit_review = db.review.insert_one({
                        "sender_id": ObjectId(sender),
                        "receiver_id": agent["_id"],
                        "review": review
                    })
                    if submit_review:
                        return True
                    else:
                        return False
            else:
                return False
        else:
            return False