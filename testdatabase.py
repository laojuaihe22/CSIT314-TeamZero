from pymongo import MongoClient

client = MongoClient("mongodb+srv://mongo:mongo@cluster0.zj42wez.mongodb.net/")

# Access a specific database
db = client["CSIT314"]

# Access a specific collection within the database
collection = db["User"]

email = "admin2@gmail.com"

user_data = {
                "email": email,
                "password": "1",
                "profile":{}
            }

collection.insert_one(user_data)  

