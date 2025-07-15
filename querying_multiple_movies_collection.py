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

# query by ObjectId
documents_to_find = {"rated": "TV-G"}

cursor = movies_collection.find(documents_to_find)

num_docs = 0
for document in cursor:
    num_docs += 1
    pprint(document)
    print()
print(f"Number of documents found: {num_docs}")

client.close()
