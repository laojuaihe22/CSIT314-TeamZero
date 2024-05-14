from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

# Access a specific database
db = client["CSIT314"]

# Access a specific collection within the database
collection = db["User"]
property_collection = db["PropertyListing"]

email = "rea@gmail.com"

user = collection.find({"email":email})

for document in user:
    print(document["_id"])