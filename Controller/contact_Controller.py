from Controller.user_Controller import user_Controller
from PyConnection.db_Controller import connect_database
from Model.user import user

class contact_Controller:
    def __init__(self):
        self.db = connect_database()
        print(self.db)

    def create_contact(self, name:str, lastname:str, location:str, number:str, email:str):
        controller = user_Controller()
        current_username = controller.username_get_capture
        existing_user = self.db.users.find_one({"username": current_username})
        print("Username: ", existing_user)
        if not existing_user:
            print("User not found")
        else:
            user_instance = user()
            user_instance.create_contact(name, lastname, location, number, email)

