from pymongo import MongoClient
from bson import ObjectId
class Rating:
    
    def __init__(self):
        self.database = None
        
        
    def get_database(self):
        if self.database is None:
            # Establish a connection to the MongoDB server
            # self.database = MongoClient("mongodb+srv://mongo:mongo@cluster0.zj42wez.mongodb.net/")
            self.database = MongoClient("mongodb+srv://mongo:mongo@cluster0.zj42wez.mongodb.net/?tls=true")
        return self.database
    
    #194 As a real estate agent, I want to view my ratings, so that I can see how satisfied my clients are and improve my services if needed.
    def viewRatingByagentId(self,agentId):
        client = self.get_database()
        db = client["CSIT314"]
        
        agent = db.UserAccount.find_one({"_id":ObjectId(agentId)})
        
        if agent:
            rating_list = list(db.Rating.find({"receiver_id":ObjectId(agentId)}))
            
            if rating_list:
                return rating_list
            else:
                return False;
    #260 As a buyer, I want to submit a rating for real estate agents in the system so that I can share my satisfaction and experience with their services
    #323 As a seller, I want to submit a rating for real estate agents in the system so that I can share my satisfaction and experience with their services.
    def submitRating(self, agent_email, sender_id, buyer_rating):
        client = self.get_database()
        db = client["CSIT314"]

        
        agent = db.UserAccount.find_one({"email": agent_email})

        if agent:
            agent_id = agent["_id"]

            profile_info = db.UserProfile.find_one({"userAccountId": agent_id})

            if profile_info and profile_info["role"] == "rea":
                
                submit_rating = db.Rating.insert_one({
                    "sender_id": ObjectId(sender_id),
                    "receiver_id": agent["_id"],
                    "rating": buyer_rating,
                })

                if submit_rating:
                    return True
                else:
                    return False