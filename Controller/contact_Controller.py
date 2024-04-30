from PyConnection.db_Controller import connect_database
from Controller.user_Controller import user_Controller
from Model.user import user

class contact_controller():
    def __init__(self):
        self.db = connect_database()

    def create_contact(self, user_username:str, name:str, lastname:str, location:str, number:str, email:str):
        controller = user_Controller
        current_username = controller.get_capture()
        if user_username == current_username:
            existing_user = self.db.users.find_one({"username": user_username})
            if existing_user:
                user_instance = user(existing_user["name"], existing_user["lastname"], existing_user["location"],
                                     existing_user["number"], existing_user["email"])
                user_instance.create_contact(name, lastname, location, number, email)
            else:
                print("User not found")