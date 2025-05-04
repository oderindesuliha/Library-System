from Library.author import Author
from Library.book import Book
from Library.user import User

class Library:

    def __init__(self):
        self.books = []
        self.borrowed_books:dict[str,User] = {}

    def add_book(self, title: str, author: Author):
        book = Book(title, author)
        self.books.append(book)

    def borrow_book(self, title: str, user: User, author: Author):
        for book in self.books:
            book_author = book.author
            if book.title == title and book.author.__str__() == author.__str__():
                # self.books.remove(book)
                print(book.is_available())
                book.is_available(False)
                self.borrowed_books[book.title] = user
                return "Book has been borrowed"

        raise ValueError(f"Book '{title}' is not in the library")

    def check_availability(self, title: str):
        for book in self.books:
            if book.title == title:
                return True
        return False

