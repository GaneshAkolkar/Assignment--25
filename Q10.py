class SmartPhone(Calculator2, Phone):
    def __init__(self):
        super().__init__()
        self.truecaller = Truecaller()

    def fetch_contact_name(self, number):
        return self.truecaller.fetch_name(number)
