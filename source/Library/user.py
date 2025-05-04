class User:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.borrowed_books = []

    @property
    def first_name(self):
        return self.first_name

    @first_name.setter
    def first_name(self, value):
        self.first_name = value

    def last_name(self):
        return self.last_name

    def age(self):
        return self.age

    def borrowed_books(self):
        return self.borrowed_books

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"




