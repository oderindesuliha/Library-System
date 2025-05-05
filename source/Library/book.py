import random

from Library.author import Author



def generate_isbn() -> str:
    prefix = "ISBN-"
    check_digit = str(random.randint(1000, 9999))
    return f"{prefix}-{check_digit}"

class Book:
    def __init__(self, title: str, author: "Author"):
        self._title = title
        self._author = author
        self.is_available = False
        self.isbn = generate_isbn()

    @property
    def title(self) -> str:
        return f'Title: {self._title}'

    @title.setter
    def title(self, value):
        self.title = value

    @property
    def author(self):
        return f'Author: {self._author}'

    @author.setter
    def author(self, value):
        self.author = value


    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) {'Available' if self.is_available else 'Not Available'}"
