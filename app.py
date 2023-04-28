from fastapi import FastAPI, HTTPException
from pymongo import MongoClient

from model_egg import ModelEgg
from immat_parser import (
    egg_parser,
    extract_day,
    extract_country,
    extract_month,
    extract_weight,
)

MONGODB_URL = "mongodb"
DB_NAME = "warehouse"

client = MongoClient(MONGODB_URL)
db = client[DB_NAME]

EGG_COLLECTION = "egg"

app = FastAPI()


@app.get("/eggs")
async def find_eggs():
    eggs = db[EGG_COLLECTION].find()
    return [egg_parser(egg) for egg in eggs]


@app.post("/eggs")
async def create_egg(egg: ModelEgg):
    e = db[EGG_COLLECTION].find_one({"registration": egg.registration})
    if e:
        raise HTTPException(
            status_code=409, detail="Egg already exists for this given registration."
        )

    db[EGG_COLLECTION].insert_one(dict(egg))
    return dict(egg)


@app.get("/eggs/immatriculation/{registration}")
async def get_egg(registration: str):
    egg = db[EGG_COLLECTION].find_one({"registration": registration})
    return egg_parser(egg) | {
        "weight": extract_weight(egg["registration"]),
        "country": extract_country(egg["registration"]),
        "day": extract_day(egg["registration"]),
        "month": extract_month(egg["registration"]),
    }


@app.put("/eggs/immatriculation/{registration}")
async def update_egg(registration: str, egg: ModelEgg):
    e = db[EGG_COLLECTION].find_one_and_update(
        {"registration": registration},
        {"$set": dict(egg)},
    )
    return egg_parser(e)


@app.delete("/eggs/immatriculation/{registration}")
async def delete_egg(registration: str):
    db[EGG_COLLECTION].delete_one({"registration": registration})
    return {"status": "ok"}
