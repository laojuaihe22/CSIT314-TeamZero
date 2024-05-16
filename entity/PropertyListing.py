from pymongo import MongoClient
from bson import ObjectId
class PropertyListing:
    def __init__(self):
        self.database = None
        
        
    def get_database(self):
        if self.database is None:
            # Establish a connection to the MongoDB server
            # self.database = MongoClient("mongodb+srv://mongo:mongo@cluster0.zj42wez.mongodb.net/")
            self.database = MongoClient("mongodb://localhost:27017")
            
        return self.database
    
    #create property listing
    def createPropertyListing(self, agentId, sellerEmail, propertyName, address, region, price, type, description, bedroom, bathroom):

        client = self.get_database()
        
        db = client["CSIT314"]
        
    
        seller = db.UserAccount.find_one({"email":sellerEmail})
        
        if not seller:
            return False
        
        # Create the property listing document      
        property_listing = {
            'agentID': ObjectId(agentId),
            'sellerID': seller["_id"],
            'propertyName': propertyName,
            'address': address,
            'region': region,
            'price': price,
            'type': type,
            'description': description,
            'bedroom': bedroom,
            'bathroom': bathroom,
            'status': 'unsold',
            'totalviews': 0,
            'shortlisted': 0,
        }

        # Insert the property listing into the propertyListing collection
        db.propertyListing.insert_one(property_listing)
            
        return True
        
            
    #view property listing
    def viewAllPropertyListing(self):
 
        client = self.get_database()
        
        db = client["CSIT314"]
        
        pipeline = [
            {
                '$lookup': {
                    'from': 'UserAccount',
                    'localField': 'agentID',
                    'foreignField': '_id',
                    'as': 'userInfo'
                }
            },
            {
                '$unwind': '$userInfo'
            }
        ]

        propertyListing = list(db.propertyListing.aggregate(pipeline))

        return propertyListing
    
        #view property listing
    def viewPropertyListingbyAgentId(self,agentId):
 
        client = self.get_database()
        
        db = client["CSIT314"]
        
        agent = db.UserAccount.find_one({"_id":ObjectId(agentId)})
        
        if not agent:
            return False

        propertyListing = list(db.propertyListing.find({"agentID":ObjectId(agentId)}))
        
        if propertyListing:
            return propertyListing
        else:
            return False
    
    #update property listing
    def updatePropertyListing(self, address, field, value):

        client = self.get_database()
        
        db = client["CSIT314"]
        
        property_doc = db.propertyListing.find_one({'address':address})
        
        if property_doc:
            update_query = {"$set": {field: value}}
            db.propertyListing.update_one({"address": address}, update_query)
            updated_property = db.propertyListing.find_one({'address': address})
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
            target_property = list(collection.find({'price': {'$lte': int(value)}})) # price less than or equal to provided value

        elif filter == 'region':
            target_property = list(collection.find({'region': value}))

        if not target_property:
            return None  
        
        return target_property
        
    
    def appendFavouriteList(self, buyerID, propertyID):
        client = self.get_database()
        db = client["CSIT314"]

        # Insert the document into the Favourite collection
        inserted = db.Favourite.insert_one({"buyerID": buyerID, "propertyID": propertyID})

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
        
    
    

    def buyerViewFavouritePropertyListing(self,buyer_id):
        client = self.get_database()
        db = client["CSIT314"]
        
        pipline = [
        {
            '$match': {
                'buyerID': buyer_id,
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
        
        property_list = db.Favourite.aggregate(pipline)
        
        if property_list:
            return property_list
        else:
            return False
    
