from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

# Access a specific database
db = client["CSIT314"]

# Access a specific collection within the database
collection = db["User"]

email = "admin2@gmail.com"

user = collection.find_one({"email": email})  

# print(user["email"]) 
# print(user["role"]) 
# print(user["profile"]['name']) 

