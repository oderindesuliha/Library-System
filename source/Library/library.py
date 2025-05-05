from Library.author import Author
from Library.book import Book
from Library.user import User

class Library:

    def __init__(self):
        self.books = []
        self.borrowed_books = {}

    def add_book(self, title: str, author: Author):
        book = Book(title, author)
        self.books.append(book)

    def borrow_book(self, title: str, user: User, author: Author):
        for book in self.books:
            if book.title == title and book.author == author and book.is_available():
                book.borrow_book(user, author)
                if not book.is_available:
                    raise ValueError(f"'{title}' is already borrowed")
                book.is_available(False)
                self.borrowed_books[book.title] = user
                user.borrowed_books.append(book)
                return "Book has been borrowed"

        raise ValueError(f"'{title}' is not in the library")

    def check_availability(self):
        for book in self.books:
            if book.is_available == is_available:
                return book.is_available
        return False

