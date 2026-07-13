"""
member.py

This module contains the Member class.

The Member class stores all the information related to a library member.
It also keeps track of all the books currently borrowed by the member.
"""


class Member:
    """
    Represents a library member.
    """

    # Maximum books a member can borrow
    MAX_BOOK_LIMIT = 5

    def __init__(self, member_id, name):
        """
        Initialize a Member object.

        Parameters:
            member_id (str): Unique member ID
            name (str): Member name
        """

        # Store member details
        self.member_id = member_id
        self.name = name

        # List to store borrowed book ISBNs
        self.borrowed_books = []

    def borrow_book(self, isbn):
        """
        Add a borrowed book to the member's record.

        Parameters:
            isbn (str): ISBN of the borrowed book

        Returns:
            tuple(bool, str)
        """

        # Check borrowing limit
        if len(self.borrowed_books) >= Member.MAX_BOOK_LIMIT:
            return False, "Borrowing limit reached."

        # Prevent duplicate entries
        if isbn in self.borrowed_books:
            return False, "Book already exists in borrowed list."

        # Add the book ISBN
        self.borrowed_books.append(isbn)

        return True, "Book added to member record."

    def return_book(self, isbn):
        """
        Remove a returned book from member record.

        Parameters:
            isbn (str): ISBN of returned book

        Returns:
            tuple(bool, str)
        """

        # Check if the member actually borrowed this book
        if isbn not in self.borrowed_books:
            return False, "This member did not borrow the book."

        # Remove book from borrowed list
        self.borrowed_books.remove(isbn)

        return True, "Book removed from member record."

    def borrowed_count(self):
        """
        Returns total number of borrowed books.
        """

        return len(self.borrowed_books)

    def can_borrow(self):
        """
        Check whether member can borrow another book.

        Returns:
            bool
        """

        return len(self.borrowed_books) < Member.MAX_BOOK_LIMIT

    def to_dict(self):
        """
        Convert Member object into dictionary.

        Used while saving JSON data.
        """

        return {
            "member_id": self.member_id,
            "name": self.name,
            "borrowed_books": self.borrowed_books
        }

    @classmethod
    def from_dict(cls, data):
        """
        Create Member object from dictionary.
        """

        member = cls(
            data["member_id"],
            data["name"]
        )

        member.borrowed_books = data["borrowed_books"]

        return member

    def __str__(self):
        """
        Return formatted member information.
        """

        return (
            f"\nMember ID : {self.member_id}"
            f"\nName      : {self.name}"
            f"\nBorrowed  : {len(self.borrowed_books)}"
            f"\nBooks     : {self.borrowed_books}"
        )