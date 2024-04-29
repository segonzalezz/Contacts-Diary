from Model.person import person
class user(person):
    def __init__(self, name, lastname, location, phone, username, password):
        super().__init__(name, lastname, location, phone)
        self._username = username
        self._password = password
        self._contacts = {}

    def create_contact(self, name, lastname, location, number, email):
        if number in self._contacts:
            print("The contact already exist")
        else:
            self._contacts = {
                            name,
                            lastname,
                            location,
                            number,
                            email
                              }
            #Colocar en tkinder este mensaje
            print("Correct successfully")

    def read_contact(self):
        return self._contacts

    def update_contact(self, name, lastname, location, number, email):
        if name not in self._contacts:
            print("Contact not found")
        else:
            self._contacts = {
                                name,
                                lastname,
                                location,
                                number,
                                email
                             }
    def delete_contact(self, number):
        if number not in self._contacts:
            print("Contact not found")
        else:
            del self._contacts[number]

    @property
    def get_username(self):
        return self._username

    @get_username.setter
    def set_username(self, value):
        self._username = value

    @property
    def get_password(self):
        return self._password

    @get_password.setter
    def set_password(self, value):
        self._password = value