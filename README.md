# Contacts - Diary
Okay, this project is about contact diary, so lets to check a design pattern to create project, in this case we use MVC.

## First created the packages:
- Package Model
- Package View
- Package Controller
- Package Py.Connection

The Py.Connection has the connection to db, to this project we are gonna use pymongo.

### Guide
- Show ide console in inroot to the project
- Use this setence: pip3 pymongo
- Implement the package wherever u want

Look the connection:
```python
from pymongo import MongoClient

def connect_database():
    client = MongoClient("mongodb://localhost:27017/")
    db_name = "MyDiary"
    if db_name in client.list_database_names():
        return client[db_name]
    else:
        db = client[db_name]
    return db
```


