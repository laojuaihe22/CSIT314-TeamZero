from pymongo import MongoClient
from bson import ObjectId

class SoldFavourite:
    
    def __init__(self):
        self.database = None

    def get_database(self):
        if self.database is None:
            # Establish a connection to the MongoDB server
            # self.database = MongoClient("mongodb+srv://mongo:mongo@cluster0.zj42wez.mongodb.net/")
            self.database = MongoClient("mongodb://localhost:27017")
            
        return self.database
    
    #258 As a buyer, I want to save sold property listings into a favorite list so that I can understand market trends.
    def saveSoldProperty(self, buyerID, propertyID):
        client = self.get_database()
        db = client["CSIT314"]

        existing_document = db.SoldFavouriteListing.find_one({"buyerID": ObjectId(buyerID), "propertyID": ObjectId(propertyID)})

        if existing_document:
            return False
        else:
            # Insert the document into the Favourite collection
            inserted = db.SoldFavouriteListing.insert_one({"buyerID": ObjectId(buyerID), "propertyID": ObjectId(propertyID)})
            increment_shorlisted = db.propertyListing.update_one(
                {"_id":ObjectId(propertyID)},{"$inc": {"shortlisted": 1}})

            if inserted and increment_shorlisted:
                return True
            else:
                return False
            
    #259 As a buyer, I want to view sold property favorite listings so that I can access property information.
    def buyerViewFavouriteSoldPropertyListing(self,buyer_id):
        client = self.get_database()
        db = client["CSIT314"]
        
        pipline = [
        {
            '$match': {
                'buyerID': ObjectId(buyer_id),
            }
        }, {
            '$lookup': {
                'from': 'propertyListing', 
                'localField': 'propertyID', 
                'foreignField': '_id', 
                'as': 'result'
            }
        }, {'$unwind': '$result'}
        ]
        
        property_list = list(db.SoldFavouriteListing.aggregate(pipline))
        
        if property_list:
            return property_list
        else:
            return False
        
    
    def unsaveSoldProperty(self,buyerID, propertyID):
        client = self.get_database()
        db = client["CSIT314"]

        existing_document = db.SoldFavouriteListing.find_one({"buyerID": ObjectId(buyerID), "propertyID": ObjectId(propertyID)})
        
        if not existing_document:
            return False
        else:
            deleted = db.SoldFavouriteListing.delete_one({"buyerID": ObjectId(buyerID), "propertyID": ObjectId(propertyID)})
            increment_shorlisted = db.NewFavouriteListing.update_one(
                {"_id":ObjectId(propertyID)},{"$inc": {"shortlisted": -1}})

            if deleted and increment_shorlisted:
                return True
            else:
                return False