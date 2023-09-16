class Profile:
    def __init__(self, name, email, age):
        self.__name = name
        self.__email = email
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age
