from pymongo import MongoClient
from bson import ObjectId

class NewFavourite:
    def __init__(self):
        self.database = None
        
        
    def get_database(self):
        if self.database is None:
            # Establish a connection to the MongoDB server
            # self.database = MongoClient("mongodb+srv://mongo:mongo@cluster0.zj42wez.mongodb.net/")
            self.database = MongoClient("mongodb+srv://mongo:mongo@cluster0.zj42wez.mongodb.net/")
            
        return self.database
    
    #256 As a buyer, I want to save new property listings into a favourite list so that I can track properties I'm interested.
    def saveNewProperty(self, buyerID, propertyID):
        client = self.get_database()
        db = client["CSIT314"]

        existing_document = db.NewFavouriteListing.find_one({"buyerID": ObjectId(buyerID), "propertyID": ObjectId(propertyID)})

        if existing_document:
            return False
        else:
            # Insert the document into the Favourite collection
            inserted = db.NewFavouriteListing.insert_one({"buyerID": ObjectId(buyerID), "propertyID": ObjectId(propertyID)})
            increment_shorlisted = db.propertyListing.update_one(
                {"_id":ObjectId(propertyID)},{"$inc": {"shortlisted": 1}})

            if inserted and increment_shorlisted:
                return True
            else:
                return False

        
    # 255 As a buyer, I want to view new property favourite listings so that I can easily access current property information
    def buyerViewFavouriteNewPropertyListing(self,buyer_id):
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
        
        property_list = list(db.NewFavouriteListing.aggregate(pipline))
        
        if property_list:
            return property_list
        else:
            return False

    def unsaveNewProperty(self, buyerID, propertyID):
        client = self.get_database()
        db = client["CSIT314"]

        existing_document = db.NewFavouriteListing.find_one({"buyerID": ObjectId(buyerID), "propertyID": ObjectId(propertyID)})
        if not existing_document:
            return False
        else:
            
            deleted = db.NewFavouriteListing.delete_one({"buyerID": ObjectId(buyerID), "propertyID": ObjectId(propertyID)})
            
            increment_shorlisted = db.propertyListing.update_one(
                {"_id":ObjectId(propertyID)},{"$inc": {"shortlisted": -1}})

            if deleted and increment_shorlisted:
                return True
            else:
                return False