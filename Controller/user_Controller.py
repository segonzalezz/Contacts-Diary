from PyConnection.db_Controller import connect_database
from Model.user import user

class user_Controller:
    def __init__(self):
        self.db = connect_database()

    def create_user(self, name:str, lastName:str, location:str, phone:int, username:str, password:str):
        existing_user = self.db.users.find_one({"username": username})
        if existing_user:
            print("User already exists in the database")
        else:
            test_user = user(name, lastName, location, phone, username, password)
            user_info = {
                "name" : test_user.get_name,
                "lastName" : test_user.get_lastName,
                "location" : test_user.get_location,
                "phone" : test_user.get_phone,
                "username" : test_user.get_username,
                "password" : test_user.get_password,
            }
            self.db.users.insert_one(user_info)

    def login_user(self, username:str, password:str):
        username = user.get_username
        existing_user = self.db.users.find_one({"username":username, "password":password})
        if existing_user:
            return True
        else:
            return False

    def username_get_capture(self):
        return self.user_get_capture
