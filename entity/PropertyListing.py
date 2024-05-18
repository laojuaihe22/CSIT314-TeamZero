from pymongo import MongoClient
from bson import ObjectId
class PropertyListing:
    def __init__(self):
        self.database = None
        
        
    def get_database(self):
        if self.database is None:
            self.database = MongoClient("mongodb://localhost:27017")
            
        return self.database
    
    #189 As a real estate agent, I want to create property listings so that buyers can find all the information they need.
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
        
    #190 As a real estate agent, I want to view property listings in my account, so that I can stay updated on their status.
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
    
    #191 As a real estate agent, I want to update property listings, so that I can ensure all information is accurate and current.
    def updatePropertyListing(self, address, field, value):

        client = self.get_database()
        
        db = client["CSIT314"]
        
        property_doc = db.propertyListing.find_one({'address':address})
        
        if property_doc:
            update_query = {"$set": {field: value}}
            db.propertyListing.update_one({"address": address}, update_query)
            
            return True
        else:
            return False
    
    #192 As a real estate agent, I want to delete property listings, so that I can remove outdated or sold properties from the database.
    def deletePropertyListing(self, address):

        client = self.get_database()
        
        db = client["CSIT314"]  
        collection = db["propertyListing"]

        delete_result = collection.delete_one({"address": address})
        if delete_result:
            return True  # Document successfully deleted
        else:
            return False  # Document not found or not deleted
        
    #search property listing
    def searchPropertyListingbyAgentId(self, agentID, filter_type, value):
        client = self.get_database()
        
        db = client["CSIT314"]
        collection = db["propertyListing"]
    

        if filter_type == 'type':
            target_property =list(collection.find({'agentID':ObjectId(agentID), 'type':value})) # landed, condo, hdb

        elif filter_type == 'price':
            target_property = list(collection.find({'agentID':ObjectId(agentID),'price': {'$lte': int(value)}})) # price less than or equal to provided value

        elif filter_type == 'region':
            target_property = list(collection.find({'agentID':ObjectId(agentID),'region': value}))

        return target_property
    
    #366 As a buyer, I want to view all property listings so that I can access property information.
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
        
        if propertyListing:
            increment_view = db.propertyListing.update_many({},{"$inc": {"totalviews": 1}})
            return propertyListing
        else:
            return False
    
    #254 As a buyer, I want to search all property listings so that I can easily find properties using keywords.
    def buyer_search_property(self,region,property_type,price_sort,status):
        
        client = self.get_database()
        db = client["CSIT314"]
        
        
        # Sort the results based on the price_sort value
        sort_order = None
        if price_sort == 'asc':
            sort_order = [('price', 1)]
        elif price_sort == 'desc':
            sort_order = [('price', -1)]
        
        property_list = list(db.propertyListing.find({"region":region,"type":property_type,"status":status}).sort(sort_order))
        
        if property_list:   
            return property_list
        else:
            return False
    
    #325 As a seller, I want to search my property listings so that I can easily find properties using keywords.
    def seller_search_property(self,sellerId,region,property_type,price_sort,status):
        client = self.get_database()
        db = client["CSIT314"]
        
        
        # Sort the results based on the price_sort value
        sort_order = None
        if price_sort == 'asc':
            sort_order = [('price', 1)]
        elif price_sort == 'desc':
            sort_order = [('price', -1)]
        
        property_list = list(db.propertyListing.find({"sellerID":ObjectId(sellerId),"region":region,"type":property_type,"status":status}).sort(sort_order))
        
        if property_list:
            return property_list
        else:
            return False
    
    #320 As a seller, I want to view all my properties so that I can easily manage and track the properties I own.
    def viewPropertyListingbySellerId(self,seller_id):
 
        client = self.get_database()
        
        db = client["CSIT314"]
        
        agent = db.UserAccount.find_one({"_id":ObjectId(seller_id)})
        
        if not agent:
            return False

        propertyListing = list(db.propertyListing.find({"sellerID":ObjectId(seller_id)}))
        
        if propertyListing:
            return propertyListing
        else:
            return False
            
            
        
       


    
