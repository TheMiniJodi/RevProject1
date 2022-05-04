
import pymongo
from pymongo import MongoClient

client = MongoClient(serverSelectionTimeoutMS = 1000)

db = client.project1

collection = db.coffee




