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
            
    def saveSoldProperty(self, buyerID, propertyID):
        client = self.get_database()
        db = client["CSIT314"]

        existing_document = db.SoldFavouriteListing.find_one({"buyerID": ObjectId(buyerID), "propertyID": ObjectId(propertyID)})

        if existing_document:
            return False
        else:
            # Insert the document into the Favourite collection
            inserted = db.SoldFavouriteListing.insert_one({"buyerID": ObjectId(buyerID), "propertyID": ObjectId(propertyID)})

            if inserted:
                return True
            else:
                return False
            
            
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
        print(1)
        if property_list:
            return property_list
        else:
            return False