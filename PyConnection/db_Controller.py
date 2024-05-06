#from pymongo import MongoClient
import pymongo
def connect_database():
    client =pymongo.MongoClient("mongodb://localhost:27017/")
    db_name = "MyDiary"
    if db_name in client.list_database_names():
        return client[db_name]
    else:
        db = client[db_name]
    return db

