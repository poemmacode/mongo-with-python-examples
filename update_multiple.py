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
selected_movies = {"runtime": 13}

# update operation

set_field = {"$set": {"runtime": 2}}


result = movies_collection.update_many(selected_movies, set_field)

pprint("Documents matched:"+str(result.matched_count))
pprint("Documents updated:"+str(result.modified_count))
pprint(movies_collection.find_one(selected_movies))

client.close()
