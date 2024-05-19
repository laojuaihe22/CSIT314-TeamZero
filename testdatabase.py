from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("mongodb://localhost:27017")

db = client["CSIT314"]


pipeline = [
    {
        '$lookup': {
            'from': 'UserProfile', 
            'localField': '_id', 
            'foreignField': 'userAccountId', 
            'as': 'result'
        }
    }, {
        '$unwind': {
            'path': '$result'
        }
    }
]

userdata = db.UserAccount.aggregate(pipeline)

print(userdata)

for doc in userdata:
    print(doc)