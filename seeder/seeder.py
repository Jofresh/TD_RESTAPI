import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

# Database information
MONGO_CLIENT = "mongodb:27017"
DB_NAME = "warehouse"
EGG_COL = "egg"
client = MongoClient(MONGO_CLIENT)
db = client[DB_NAME]

VALID_REGISTRATIONS = ["05-FR12301FE", "25-BE44212JA"]
INVALID_REGISTRATIONS = [
    "12-FR12301FE",
    "05 FR12301FE",
    "05-ZZ12301FE",
    "05-FR12101FE",
    "05-FR12399FE",
    "05-FR12301ZZ",
    "05-FR12302FE",
]

# Populating database
registrations = VALID_REGISTRATIONS + INVALID_REGISTRATIONS
eggs_to_insert = [
    {
        "_id": ObjectId(),
        "origin": "farm",
        "color": "yellow",
        "registration": registration,
    }
    for registration in registrations
]

db[EGG_COL].insert_many(eggs_to_insert)
