from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("mongodb://localhost:27017")

db = client["CSIT314"]



# target_property =list(collection.find({'type':value})) # landed, condo, hdb


# target_property = list(collection.find({'price': {'$lte': int(value)}})) # price less than or equal to provided value


target_property = list(db.propertyListing.find())


print(target_property)