class Truecaller:
    def __init__(self):
        self.contacts = {}

    def fetch_name(self, number):
        return self.contacts.get(number, "Name not found")

    def add_entry(self, number, name):
        self.contacts[number] = name
