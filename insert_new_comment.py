from pymongo import MongoClient
import datetime
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

db = client.sample_mflix

comments_collection = db.comments

new_comment = {
    "name": "Emma Nicole",
    "email": "poemmaestrada@gmail.com",
    "movie_id": "573a1390f29313caabcd4323",
    "text": "Eius veritatis vero facilis quaerat fuga temporibus. Praesentium expedita sequi repellat id. Corporis minima enim ex. Provident fugit nisi dignissimos nulla nam ipsum aliquam.",
    "date": datetime.datetime.utcnow(),
}

result = comments_collection.insert_one(new_comment)

document_id = result.inserted_id
print(f"_id of inserted document: {document_id}")

client.close()
