#!/usr/bin/env python3

from pymongo import MongoClient

mongo_con = MongoClient()

db = mongo_con["flask-app"]


# Inserindo subdocumento

# inserted = db.user.update_one(
#     {
#         "messages.name": "usuario_name"
#     },
#     {
#         "$push":{
#             "messages":{
#                 "name": "usuario_name",
#                 "message": "mensagem"
#             }
#         }
#     }
# )
# print(inserted.matched_count, inserted.modified_count)

# Atualizando subdocumento

# updated = db.user.update_one(
#     {
#         "messages.name": "usuario_name"
#     },
#     {
#         "$set":{
#             "messages.$.name": "Thiago"
#         }
#     }
# )
# print(updated.matched_count, updated.modified_count)

# Removendo Subdocumento

removed = db.user.update_one(
    {
        "name": "usuario_name"
    },
    {
        "$pull":{
            "messages":{
                "name": "usuario_name"
            }
        }
    }
)

print(removed.matched_count, removed.modified_count)