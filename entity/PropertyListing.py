from pymongo import MongoClient

class PropertyListing:
    def __init__(self):
        self.database = None
        
        
    def get_database(self):
        if self.database is None:
            # Establish a connection to the MongoDB server
            self.database = MongoClient("mongodb+srv://mongo:mongo@cluster0.zj42wez.mongodb.net/")
        return self.database
    
    #create property listing
    def createPropertyListing(self, agentID, region, address, price, type, description):

        client = self.get_database()
        
        db = client["CSIT314"]
        collection = db["propertyListing"]

        collection.insert_one({'agentID':agentID, 'address' : address, 'region': region, 'price':price, 'type': type, 'description' : description })
        return True

    #view property listing
    def viewPropertyListing(self):

        client = self.get_database()
        
        db = client["CSIT314"]
        collection = db["propertyListing"]

        propertyListing = list(collection.find())
        
        return propertyListing
    
    #update property listing
    def updatePropertyListing(self, address, field, value):

        client = self.get_database()
        
        db = client["CSIT314"]
        collection = db["propertyListing"]

        property_doc = collection.find_one({'address':address})
        
        if property_doc:
            update_query = {"$set": {field: value}}
            collection.update_one({"address": address}, update_query)
            updated_property = collection.find_one({'address': address})
            return updated_property
        else:
            return None
    
    #delete property listing
    def deletePropertyListing(self, address):

        client = self.get_database()
        
        db = client["CSIT314"]  
        collection = db["propertyListing"]

        delete_result = collection.delete_one({"address": address})
    
        if delete_result.deleted_count > 0:
            return True  # Document successfully deleted
        else:
            return False  # Document not found or not deleted
        
    #search property listing
    def searchPropertyListing(self, filter, value):
        client = self.get_database()
        
        db = client["CSIT314"]
        collection = db["propertyListing"]

        if filter == 'type':
            target_property =list(collection.find({'type':value})) # landed, condo, hdb

        elif filter == 'price':
            target_property = list(collection.find({'price': {'$lte': value}})) # less than or equal to price
        
        elif filter == 'region':
            
            target_property =list(collection.find({'region':value})) # north, south, east, west
            return target_property
        
        if not target_property:
            return None  
        
        return target_property
        


