# $match $group
# Find all accounts with a balance of less than $1000
# Group accounts by account type
# Calculate the average balance for each account type

# pipeline = [<stage 1>, <stage 2>, <stage 3>]
# db.collection,aggregate(pipeline)
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

# get referece to movies collection
movies_collection = db.movies

# select movies with a runtime less than 100 minutes

select_by_runtime = {"$match": {"runtime": {"$lt": 100}}}

# separate movies by their rating
separate_by_rating = {"$group": {
    "_id": "$rated",
    "average_runtime": {"$avg": "$runtime"},
    "total_movies": {"$sum": 1}
}}

# create an aggregation pipeline
pipeline = [select_by_runtime, separate_by_rating]
# execute the aggregation pipeline
results = movies_collection.aggregate(pipeline)

print()
print("Movies with a runtime less than 100 minutes, grouped by rating:", "\n")

for item in results:
    pprint(item)


client.close()
