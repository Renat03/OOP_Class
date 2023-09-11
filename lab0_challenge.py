class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastName = lastname

    def convert(self, firstname, lastname):
        print(f"{firstname[0]}. {lastname[0]}.")


person = User("John", "Smith")
person.convert("John", "Smith")