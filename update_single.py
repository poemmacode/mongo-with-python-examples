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

movies_collection = db.movies

# filter
document_to_update = {"_id": ObjectId("573a1390f29313caabcd42e8")}

# update operation

add_to_runtime = {"$inc": {"runtime": 2}}

pprint(movies_collection.find_one(document_to_update))

result = movies_collection.update_one(document_to_update, add_to_runtime)

pprint("Number of documents updated:"+str(result.modified_count))

client.close()
