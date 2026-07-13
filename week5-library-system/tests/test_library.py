"""
Unit tests for the Library class.
"""

import unittest

from library_system.library import Library


class TestLibrary(unittest.TestCase):
    """
    Test cases for Library class.
    """

    def setUp(self):
        """
        Create a new Library object before every test.
        """

        self.library = Library()

        # Add sample book
        self.library.add_book(
            "Python Programming",
            "John Smith",
            "ISBN001",
            2024
        )

        # Register sample member
        self.library.register_member(
            "M001",
            "Dee"
        )

    def test_add_book(self):
        """
        Test adding a new book.
        """

        success, message = self.library.add_book(
            "Java",
            "James",
            "ISBN002",
            2023
        )

        self.assertTrue(success)
        self.assertEqual(len(self.library.books), 2)

    def test_register_member(self):
        """
        Test registering a member.
        """

        success, message = self.library.register_member(
            "M002",
            "Alex"
        )

        self.assertTrue(success)
        self.assertEqual(len(self.library.members), 2)

    def test_borrow_book(self):
        """
        Test borrowing a book.
        """

        success, message = self.library.borrow_book(
            "M001",
            "ISBN001"
        )

        self.assertTrue(success)
        self.assertFalse(
            self.library.books["ISBN001"].available
        )

    def test_return_book(self):
        """
        Test returning a borrowed book.
        """

        self.library.borrow_book(
            "M001",
            "ISBN001"
        )

        success, message = self.library.return_book(
            "M001",
            "ISBN001"
        )

        self.assertTrue(success)
        self.assertTrue(
            self.library.books["ISBN001"].available
        )

    def test_search_book(self):
        """
        Test searching by title.
        """

        books = self.library.search_by_title("Python")

        self.assertEqual(len(books), 1)

    def test_statistics(self):
        """
        Test statistics generation.
        """

        stats = self.library.get_statistics()

        self.assertEqual(stats["Total Books"], 1)
        self.assertEqual(stats["Registered Members"], 1)


if __name__ == "__main__":
    unittest.main()