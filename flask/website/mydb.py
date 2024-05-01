from pymongo import MongoClient

client = MongoClient("localhost", 27017)

db = client.mydb #db

users = db.users #collection


