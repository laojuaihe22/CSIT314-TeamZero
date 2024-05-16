from pymongo import MongoClient
from bson import ObjectId

class Favourite:
    def __init__(self):
        self.database = None
        
        
    def get_database(self):
        if self.database is None:
            # Establish a connection to the MongoDB server
            # self.database = MongoClient("mongodb+srv://mongo:mongo@cluster0.zj42wez.mongodb.net/")
            self.database = MongoClient("mongodb://localhost:27017")
            
        return self.database
    
    def appendFavouriteList(self, buyerID, propertyID):
        client = self.get_database()
        db = client["CSIT314"]

        existing_document = db.Favourite.find_one({"buyerID": ObjectId(buyerID), "propertyID": ObjectId(propertyID)})

        if existing_document:
            return False
        else:
            # Insert the document into the Favourite collection
    
            inserted = db.Favourite.insert_one({"buyerID": ObjectId(buyerID), "propertyID": ObjectId(propertyID)})

            if inserted:
                return True
            else:
                return False
                
        


    def shortlistedIncrement(self, propertyID):
        client = self.get_database()
        db = client["CSIT314"]
        objID = ObjectId(propertyID)
        
        property_doc = db.propertyListing.find_one({"_id": objID})
        
        if property_doc:
            new_shortlisted_count = property_doc.get("shortlisted", 0) + 1
            increment = {"$set": {"shortlisted": new_shortlisted_count}}
            
            # Use objID instead of propertyID in the update query
            db.propertyListing.update_one({"_id": objID}, increment)
            return True
        else:
            return False