class Note:

    def __init__(self, name, surname, phone, birthday):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.birthday = birthday

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError
        self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise TypeError
        self.__surname = surname

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        if not isinstance(phone, str):
            raise TypeError
        self.__phone = phone

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, birthday):
        if not isinstance(birthday, str):
            raise TypeError
        self.__birthday = birthday

    def __str__(self):
        return f"{self.name} {self.surname}, phone number: {self.phone}, birthday date: {self.birthday}"
