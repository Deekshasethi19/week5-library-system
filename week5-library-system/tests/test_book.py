"""
Unit tests for the Book class.
"""

import unittest
from library_system.book import Book


class TestBook(unittest.TestCase):
    """
    Test cases for Book class.
    """

    def setUp(self):
        """
        Create a Book object before every test.
        """
        self.book = Book(
            "Python Programming",
            "John Smith",
            "ISBN001",
            2024
        )

    def test_book_creation(self):
        """
        Test whether book attributes are initialized correctly.
        """
        self.assertEqual(self.book.title, "Python Programming")
        self.assertEqual(self.book.author, "John Smith")
        self.assertEqual(self.book.isbn, "ISBN001")
        self.assertTrue(self.book.available)

    def test_borrow_book(self):
        """
        Test borrowing a book.
        """
        success, message = self.book.borrow("M001")

        self.assertTrue(success)
        self.assertFalse(self.book.available)
        self.assertEqual(self.book.borrowed_by, "M001")

    def test_return_book(self):
        """
        Test returning a borrowed book.
        """
        self.book.borrow("M001")
        success, message = self.book.return_book()

        self.assertTrue(success)
        self.assertTrue(self.book.available)

    def test_to_dict(self):
        """
        Test dictionary conversion.
        """
        data = self.book.to_dict()

        self.assertIsInstance(data, dict)
        self.assertEqual(data["title"], "Python Programming")

    def test_from_dict(self):
        """
        Test object creation from dictionary.
        """
        data = self.book.to_dict()

        new_book = Book.from_dict(data)

        self.assertEqual(new_book.title, self.book.title)
        self.assertEqual(new_book.author, self.book.author)


if __name__ == "__main__":
    unittest.main()