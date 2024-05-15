from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("mongodb+srv://mongo:mongo@cluster0.zj42wez.mongodb.net/")

# Access a specific database
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

result = list(db.propertyListing.aggregate(pipeline))

for doc in result:
    print()
    print(doc)
