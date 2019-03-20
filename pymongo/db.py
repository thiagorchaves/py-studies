#!/usr/bin/env python3

from pymongo import MongoClient

mongo_con = MongoClient()

db = mongo_con["flask-app"]

inserted = db.user.insert_one(
    {
        "name": "usuario_name",
        "email": "usuario_email",
        "messages": [
            {
                "name": "usuario_name",
                "message": "mensagem"
            }
        ]    
    }
)

print(inserted)
