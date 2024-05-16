from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("mongodb://localhost:27017")

db = client["CSIT314"]



# Sort the results based on the price_sort value
price_sort = 'desc'

if price_sort == 'asc':
    sort_order = [('price', 1)]
elif price_sort == 'desc':
    sort_order = [('price', -1)]


property_list = list(db.propertyListing.find({"region":"North","type":"Condo","status":"unsold"}).sort(sort_order))

print(property_list)