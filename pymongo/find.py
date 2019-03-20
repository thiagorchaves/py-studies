#!/usr/bin/env python3

from pymongo import MongoClient

mongo_con = MongoClient()

db = mongo_con["flask-app"]

user = db.user.find_one(
    {
        "name": "usuario_name",
        "email": "usuario_email",

    }
)
print(user)
print(user["_id"].generation_time)
