from unittest import TestCase

from Library.author import Author
from Library.book import Book
from Library.library import Library
from Library.user import User


class Test(TestCase):
    def test_library(self):
        pass

    def test_to_add_books(self):
        self.library = Library()
        self.library.add_book('Ralia The Sugar Girl', Author('Kola','Onadipe'))
        self.assertEqual(len(self.library.books), 1)


    def test_to_add_multiple_books(self):
        self.library = Library()
        self.library.add_book('Ralia The Sugar Girl', Author('Kola','Onadipe'))
        self.library.add_book('Last Days At Forcados High School', Author('A. H.' ,'Mohammed'))
        self.library.add_book('Purple Hibiscus', Author('Chimamanda Ngozi',' Adichie'))
        self.assertEqual(len(self.library.books), 3)

    def test_to_borrow_book(self):
        self.library = Library()
        self.user = User('Bola','Kayode',15)
        self.library.add_book('Ralia The Sugar Girl', Author('Kola', 'Onadipe'))
        self.library.add_book('Last Days At Forcados High School', Author('A. H.','Mohammed'))
        self.library.add_book('Purple Hibiscus', Author('Chimamanda Ngozi', 'Adichie'))
        self.assertEqual(len(self.library.books), 3)


        self.assertEqual(self.library.check_availability('Ralia The Sugar Girl'), True)
        expected = self.library.borrow_book('Ralia The Sugar Girl',User('Bola','Kayode',15) ,Author('Kola', 'Onadipe'))
        self.assertEqual(expected, "Book has been borrowed")
        self.assertEqual(len(self.library.books), 2)