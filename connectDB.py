
import pymongo
from pymongo import MongoClient

client = MongoClient()

db = client.project1

collection = db.coffee


# print(collection.find_one())