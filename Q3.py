class Profile:
    def __init__(self, name, __email, __age):
        self.__name = name
        self.__email = __email
        self.__age = __age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_email(self):
        return self.__email

    def set_email(self, __email):
        self.__email = __email

    def get_age(self):
        return self.__age

    def set_age(self, __age):
        self.__age = __age
