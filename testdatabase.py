from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("mongodb://localhost:27017")

# Access a specific database
db = client["CSIT314"]

buyer_email = "buyer@gmail.com"


pipline = [
    {
        '$match': {
            'buyerID': buyer_email
        }
    }, {
        '$lookup': {
            'from': 'propertyListing', 
            'localField': 'propertyID', 
            'foreignField': '_id', 
            'as': 'result'
        }
    }, {'$unwind': '$result'}
]

result_here = db.Favourite.aggregate(pipline)

for doc in result_here:
  
  print(doc)