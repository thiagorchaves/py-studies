from pymongo import MongoClient, DESCENDING
import time

try:
    con = MongoClient()
    db = con['chat']
except Exception as e:
    print('ERRO: {}'.format(e))
    exit()

def register_message(name, message):
    date = {
        'name': name,
        'message': message,
        'time': time.strftime('%d-%m-%Y %H:%M:%S')
    }
    db.chat.insert(date)
def find_message():
    last = [x for x in db.chat.find().sort('_id',DESCENDING)]
    while True:
        found = [x for x in db.chat.find().sort('_id',DESCENDING)]
        if found != last:
            last = found
            print("[{}] {} : {}\n".format(
                found[0]['time'], found[0]['name'], found[0]['message']
            ))
        time.sleep(2)