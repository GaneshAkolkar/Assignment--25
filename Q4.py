class Profile:
    platform = "Python"  # Class variable

    def __init__(self, name, email, age):
        self.__name = name
        self.__email = email
        self.__age = age

    @classmethod
    def get_platform(cls):
        return cls.platform
