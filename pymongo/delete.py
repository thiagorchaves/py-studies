#!/usr/bin/env python3

from pymongo import MongoClient

mongo_con = MongoClient()

db = mongo_con["flask-app"]

deleted = db.user.delete_one(
    {
        "name": "usuario_name"
    }

)
print(deleted.deleted_count)