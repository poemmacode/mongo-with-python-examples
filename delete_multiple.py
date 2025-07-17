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
documents_to_delete = {"runtime": 2}


print("Searching for target document before deletion:")
pprint(movies_collection.find_one(documents_to_delete))


result = movies_collection.delete_many(documents_to_delete)

print("Searching for target document after deletion:")

pprint(movies_collection.find_one(documents_to_delete))
pprint("Documents deleted:"+str(result.deleted_count))

client.close()
