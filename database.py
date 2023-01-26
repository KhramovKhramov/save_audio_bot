from pymongo import MongoClient
import settings
from base64 import b64encode

client = MongoClient(settings.MONGO_LINK)
db = client[settings.MONGO_DB_NAME]

def get_or_create_user(db, user_id, username):
    user = db.users.find_one({'user_id': user_id})
    
    if not user:
        user = {
            'user_id': user_id,
            'username': username
        }
        db.users.insert_one(user)
    
    return user

def save_to_db(db, current_user, file_name, folder):
    user = db.users.find_one({'user_id': current_user['user_id']})

    if folder not in user:
        with open(f'{file_name}', 'rb') as f:
            bynary = b64encode(f.read())
            file = {
            'file_name': file_name,
            'bynary': bynary}
            db.users.update_one(
            {'_id': user['_id']},
            {'$set': {folder: [file]}})

    else:
        with open(f'{file_name}', 'rb') as f:
            bynary = b64encode(f.read())
            file = {
            'file_name': file_name,
            'bynary': bynary}
            db.users.update_one(
            {'_id': user['_id']},
            {'$push': {folder: file}})