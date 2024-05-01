from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

# Access a specific database
db = client["CSIT314"]

# Access a specific collection within the database
collection = db["User"]

email = "a123@gmail.com"

user = collection.find_one({"email":email})    

if user:
    # Delete the document
    collection.delete_one({"email": email})
    print("User with email", email, "deleted successfully.")
else:
    print("User with email", email, "not found.")