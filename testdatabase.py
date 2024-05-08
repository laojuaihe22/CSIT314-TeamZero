from pymongo import MongoClient

client = MongoClient("mongodb+srv://mongo:mongo@cluster0.zj42wez.mongodb.net/")

# Access a specific database
db = client["CSIT314"]

# Access a specific collection within the database
collection = db["User"]

email = "admin3@gmail.com"

user = collection.find_one({"email":email})

# print(user["profile"]["role"])
print(user["profile"]["role"])