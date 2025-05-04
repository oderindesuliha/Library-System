import random

from Library.author import Author


def generate_isbn() -> str:
    prefix = "ISBN-"
    check_digit = str(random.randint(1000, 9999))
    return f"{prefix}-{check_digit}"

class Book:
    def __init__(self, title: str, author: "Author"):
        self.title = title
        self.author = author
        self.is_available = True
        self.isbn = generate_isbn()

    @property
    def title(self) -> str:
        return self.title

    @property
    def author(self) -> str:
        return self.author


    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', ISBN='{self.isbn}', available={self.available})"

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) {'Available' if self.available else 'Not Available'}"
