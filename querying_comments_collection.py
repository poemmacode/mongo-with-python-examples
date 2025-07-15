from pymongo import MongoClient
from pprint import pprint
from bson import ObjectId

import datetime
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)

db = client.sample_mflix

comments_collection = db.comments

# query by ObjectId
document_to_find = {"_id": ObjectId("5a9427648b0beebeb6957cd6")}

result = comments_collection.find_one(document_to_find)

pprint(result)

client.close()
