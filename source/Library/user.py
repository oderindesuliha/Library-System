class User:

    def __init__(self, first_name, last_name, age):
        self._first_name = first_name
        self._last_name = last_name
        self._age = age
        self.borrowed_books = []

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value


    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 15:
            raise ValueError("Age must be at least 15.")
        self._age = value

    def borrowed_books(self):
        return self.borrowed_books

    def __repr__(self):
        return f"{self._first_name} {self._last_name}"




