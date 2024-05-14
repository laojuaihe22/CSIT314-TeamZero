from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("mongodb://localhost:27017")

# Access a specific database
db = client["CSIT314"]

user = db.UserAccount.find_one({"email":"rea222@gmail.com"})

print(user)

# # Access a specific collection within the database
# collection_user_account = db["UserAccount"]
# collection_profile= db["UserProfile"]

# user_email = "rea@gmail.com"

# user_data = {
#     "email": user_email,
#     "password": "1",
#     "status":True
# }
# # Insert user data into the database
# collection_user_account.insert_one(user_data)

# user_acc_pk = collection_user_account.find_one({'email': user_email})

# user_profile_role = {
#     "userAccountId": user_acc_pk["_id"],
#     "role": "rea"
# }
# # Insert user data into the database
# collection_profile.insert_one(user_profile_role)
