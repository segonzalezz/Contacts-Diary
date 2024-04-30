from user_Controller import user_Controller
from PyConnection.db_Controller import connect_database
from Model.user import user

class contact_controller():
    def __init(self):
        self.db = connect_database()

    def create_contact(self, user_username:str, name:str, lastname:str, location:str, number:str, email:str):
        controller = user_Controller()
        current_username = controller.get_capture()
        if user_username == current_username:
            existing_user = self.db.users.find_one({"username": user_username})
            if existing_user:
                user_instance = user(existing_user["name"], existing_user["lastName"], existing_user["location"],
                                     existing_user["phone"], existing_user["username"], existing_user["password"])
                user_instance.create_contact(name, lastname, location, number, email)
                return True
            else:
                print("User not found")
                return False