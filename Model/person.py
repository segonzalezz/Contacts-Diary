class person:
    def __init__(self, name, lastname, location, phone):
        self._name = name
        self._lastName = lastname
        self._location = location
        self._phone = phone

    @property
    def get_name(self):
        return self._name

    @get_name.setter
    def set_name(self, value):
        self._name = value

    @property
    def get_lastname(self):
        return self._lastname

    @get_lastname.setter
    def set_lastname(self, value):
        self._lastname = value

    @property
    def get_location(self):
        return self._location

    @get_location.setter
    def set_location(self, value):
        self._location = value

    @property
    def get_phone(self):
        return self._phone

    @get_phone.setter
    def set_phone(self, value):
        self._phone = value


