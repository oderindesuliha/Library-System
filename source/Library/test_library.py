from unittest import TestCase

from Library.author import Author
from Library.library import Library
from Library.user import User


class Test(TestCase):
    def test_library(self):
        pass

    def test_to_add_books(self):
        library = Library()
        library.add_book('Ralia The Sugar Girl', Author('Kola','Onadipe'))
        self.assertEqual(len(library.books), 1)


    def test_to_add_multiple_books(self):
        library = Library()
        library.add_book('Ralia The Sugar Girl', Author('Kola','Onadipe'))
        library.add_book('Last Days At Forcados High School', Author('A. H.' ,'Mohammed'))
        library.add_book('Purple Hibiscus', Author('Chimamanda Ngozi',' Adichie'))
        self.assertEqual(len(library.books), 3)

    def test_to_borrow_book(self):
        library = Library()
        User('Bola','Kayode',15)
        library.add_book('Ralia The Sugar Girl', Author('Kola', 'Onadipe'))
        library.add_book('Last Days At Forcados High School', Author('A. H.','Mohammed'))
        library.add_book('Purple Hibiscus', Author('Chimamanda Ngozi', 'Adichie'))
        self.assertEqual(len(library.books), 3)


        self.assertEqual(library.check_availability('Ralia The Sugar Girl'), True)
        expected = library.borrow_book('Ralia The Sugar Girl',User('Bola','Kayode',15) ,Author('Kola', 'Onadipe'))
        self.assertEqual(expected, "Book has been borrowed")
        self.assertEqual(len(library.books), 2)