
# This is my database connection file
import pymongo
from pymongo import MongoClient

# If we can't connect to db then time out after 1000 miliseconds
client = MongoClient(serverSelectionTimeoutMS = 1000)

db = client.project1

collection = db.coffee




