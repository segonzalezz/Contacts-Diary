from PyConnection.db_Controller import connect_database
from Model.user import user

class user_Controller:
    def __init__(self):
        self.db = connect_database()
        self.username_get_capture = None

    def create_user(self, name:str, lastname:str, location:str, phone:int, username:str, password:str):
        existing_user = self.db.users.find_one({"username": username})
        if existing_user:
            print("User already exists in the database")
        else:
            user_info = {
                "name" : name,
                "lastName" : lastname,
                "location" : location,
                "phone" : phone,
                "username" : username,
                "password" : password,
            }
            self.db.users.insert_one(user_info)

    def login_user(self, username:str, password:str):
        existing_user = self.db.users.find_one({"username":username, "password":password})
        if existing_user:
            self.username_get_capture = existing_user
            return True
        else:
            return False

