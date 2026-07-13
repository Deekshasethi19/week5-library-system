"""
book.py

This module contains the Book class.

The Book class stores all the information related to a single book
and provides methods to issue, return and serialize the book data.
"""

# Import required modules
from datetime import datetime, timedelta


class Book:
    """
    Represents a single book in the library.
    """

    def __init__(self, title, author, isbn, publication_year):
        """
        Initialize a new Book object.

        Parameters:
            title (str): Book title
            author (str): Author name
            isbn (str): Unique ISBN number
            publication_year (int): Year of publication
        """

        # Store basic details
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year

        # True means the book is available
        self.available = True

        # Stores member id of borrower
        self.borrowed_by = None

        # Date when the book was borrowed
        self.borrow_date = None

        # Expected return date
        self.due_date = None

    def borrow(self, member_id, days=14):
        """
        Borrow this book.

        Parameters:
            member_id (str): Member borrowing the book
            days (int): Borrow duration

        Returns:
            tuple(bool, str)
        """

        # Book is already borrowed
        if not self.available:
            return False, "Book is currently unavailable."

        # Update availability
        self.available = False

        # Store borrower id
        self.borrowed_by = member_id

        # Current date
        today = datetime.now()

        # Store dates in readable format
        self.borrow_date = today.strftime("%Y-%m-%d")

        self.due_date = (
            today + timedelta(days=days)
        ).strftime("%Y-%m-%d")

        return True, "Book borrowed successfully."

    def return_book(self):
        """
        Return the borrowed book.

        Returns:
            tuple(bool, str)
        """

        # Book wasn't borrowed
        if self.available:
            return False, "Book is already available."

        # Reset all borrowing details
        self.available = True
        self.borrowed_by = None
        self.borrow_date = None
        self.due_date = None

        return True, "Book returned successfully."

    def is_overdue(self):
        """
        Check whether the due date has passed.

        Returns:
            bool
        """

        if self.available:
            return False

        due = datetime.strptime(
            self.due_date,
            "%Y-%m-%d"
        )

        return datetime.now() > due

    def overdue_days(self):
        """
        Calculate total overdue days.

        Returns:
            int
        """

        if not self.is_overdue():
            return 0

        due = datetime.strptime(
            self.due_date,
            "%Y-%m-%d"
        )

        return (datetime.now() - due).days

    def to_dict(self):
        """
        Convert object into dictionary.

        Used while saving JSON.
        """

        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "publication_year": self.publication_year,
            "available": self.available,
            "borrowed_by": self.borrowed_by,
            "borrow_date": self.borrow_date,
            "due_date": self.due_date
        }

    @classmethod
    def from_dict(cls, data):
        """
        Create Book object from dictionary.
        """

        book = cls(
            data["title"],
            data["author"],
            data["isbn"],
            data["publication_year"]
        )

        book.available = data["available"]
        book.borrowed_by = data["borrowed_by"]
        book.borrow_date = data["borrow_date"]
        book.due_date = data["due_date"]

        return book

    def __str__(self):
        """
        String representation of Book object.
        """

        status = "Available"

        if not self.available:
            status = f"Borrowed by {self.borrowed_by}"

        return (
            f"\nTitle : {self.title}"
            f"\nAuthor : {self.author}"
            f"\nISBN : {self.isbn}"
            f"\nYear : {self.publication_year}"
            f"\nStatus : {status}"
        )