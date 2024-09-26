import unittest
from library import Library, Book

class TestLibrary(unittest.TestCase):
    def test_add_book(self):
        library = Library()
        book = Book("123", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
        library.add_book(book)
        self.assertEqual(len(library.books), 1)
        self.assertIn(book, library.books)

    def test_borrow_book(self):
        library = Library()
        book = Book("123", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
        library.add_book(book)
        library.borrow_book("123")
        self.assertTrue(book.is_borrowed)

    def test_borrow_unavailable_book(self):
        library = Library()
        book = Book("123", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
        library.add_book(book)
        library.borrow_book("123")
        with self.assertRaises(Exception) as context:
            library.borrow_book("123")
        self.assertTrue('Book is already borrowed' in str(context.exception))

if __name__ == "__main__":
    unittest.main()