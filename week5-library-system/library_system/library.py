'''
Name: Deeksha Sethi
Project name: Library System
Description: The Library Management System is a Python CLI application built using OOP concepts. It manages books and members, supports borrowing and returning books, searching records, generating statistics, and storing data using JSON with backup functionality.
'''


"""
library.py

This module contains the Library class.

The Library class is responsible for managing books,
members and all library operations.
"""

# Standard library imports
import json
import os
import shutil

# Import custom classes
from book import Book
from member import Member


class Library:
    """
    Represents the complete library system.

    This class manages:
    - Books
    - Members
    - Borrowing
    - Returning
    - Saving & Loading data
    """

    def __init__(self):
        """
        Create an empty library.
        """

        # Dictionary to store books
        # Key = ISBN
        # Value = Book object
        self.books = {}

        # Dictionary to store members
        # Key = Member ID
        # Value = Member object
        self.members = {}


        # ==========================================================
    # BOOK MANAGEMENT
    # ==========================================================

    def add_book(self, title, author, isbn, publication_year):
        """
        Add a new book to the library.
        """

        # Check whether ISBN already exists
        if isbn in self.books:
            return False, "A book with this ISBN already exists."

        # Create Book object
        new_book = Book(
            title,
            author,
            isbn,
            publication_year
        )

        # Store inside dictionary
        self.books[isbn] = new_book

        return True, "Book added successfully."

    def remove_book(self, isbn):
        """
        Remove a book from the library.
        """

        # Book doesn't exist
        if isbn not in self.books:
            return False, "Book not found."

        # Don't allow deletion if borrowed
        if not self.books[isbn].available:
            return False, "Cannot remove a borrowed book."

        del self.books[isbn]

        return True, "Book removed successfully."

    def get_book(self, isbn):
        """
        Return Book object using ISBN.
        """

        return self.books.get(isbn)

        # ==========================================================
    # MEMBER MANAGEMENT
    # ==========================================================

    def register_member(self, member_id, name):
        """
        Register a new member.
        """

        # Duplicate member check
        if member_id in self.members:
            return False, "Member ID already exists."

        # Create Member object
        member = Member(member_id, name)

        # Save inside dictionary
        self.members[member_id] = member

        return True, "Member registered successfully."

    def get_member(self, member_id):
        """
        Return Member object.
        """

        return self.members.get(member_id)

    def remove_member(self, member_id):
        """
        Remove member from library.
        """

        if member_id not in self.members:
            return False, "Member not found."

        member = self.members[member_id]

        # Don't allow deletion if books are pending
        if member.borrowed_books:
            return False, "Member still has borrowed books."

        del self.members[member_id]

        return True, "Member removed successfully."

        # ==========================================================
    # BORROW & RETURN
    # ==========================================================

    def borrow_book(self, member_id, isbn):
        """
        Borrow a book.
        """

        # Validate member
        member = self.get_member(member_id)

        if member is None:
            return False, "Member not found."

        # Validate book
        book = self.get_book(isbn)

        if book is None:
            return False, "Book not found."

        # Check member borrowing limit
        if not member.can_borrow():
            return False, "Borrowing limit reached."

        # Borrow from Book class
        success, message = book.borrow(member_id)

        if not success:
            return False, message

        # Update member record
        member.borrow_book(isbn)

        return True, "Book issued successfully."

    def return_book(self, member_id, isbn):
        """
        Return a borrowed book.
        """

        member = self.get_member(member_id)

        if member is None:
            return False, "Member not found."

        book = self.get_book(isbn)

        if book is None:
            return False, "Book not found."

        # Remove from member record
        member.return_book(isbn)

        # Update book status
        success, message = book.return_book()

        return success, message

        # ==========================================================
    # SEARCH OPERATIONS
    # ==========================================================

    def search_by_title(self, keyword):
        """
        Search books by title.

        Parameters:
            keyword (str): Title or part of title

        Returns:
            list: Matching Book objects
        """

        matching_books = []

        # Loop through every book
        for book in self.books.values():

            # Ignore uppercase/lowercase differences
            if keyword.lower() in book.title.lower():
                matching_books.append(book)

        return matching_books

    def search_by_author(self, keyword):
        """
        Search books by author.
        """

        matching_books = []

        for book in self.books.values():

            if keyword.lower() in book.author.lower():
                matching_books.append(book)

        return matching_books

    def search_by_isbn(self, isbn):
        """
        Search book using ISBN.
        """

        if isbn in self.books:
            return self.books[isbn]

        return None

        # ==========================================================
    # DISPLAY FUNCTIONS
    # ==========================================================

    def display_books(self):
        """
        Display all books.
        """

        if not self.books:
            print("\nNo books available.")
            return

        for book in self.books.values():
            print(book)
            print("-" * 50)

    def display_members(self):
        """
        Display all members.
        """

        if not self.members:
            print("\nNo registered members.")
            return

        for member in self.members.values():
            print(member)
            print("-" * 50)    


        # ==========================================================
    # LIBRARY STATISTICS
    # ==========================================================

    def get_statistics(self):
        """
        Generate library statistics.

        Returns:
            dict
        """

        total_books = len(self.books)
        total_members = len(self.members)

        available_books = 0
        borrowed_books = 0
        overdue_books = 0

        # Count every book
        for book in self.books.values():

            if book.available:
                available_books += 1
            else:
                borrowed_books += 1

            if book.is_overdue():
                overdue_books += 1

        return {
            "Total Books": total_books,
            "Available Books": available_books,
            "Borrowed Books": borrowed_books,
            "Overdue Books": overdue_books,
            "Registered Members": total_members
        }


        # ==========================================================
    # SAVE DATA
    # ==========================================================

    def save_data(self):
        """
        Save all books and members into JSON files.
        """

        # Create folders if they don't exist
        os.makedirs("data", exist_ok=True)
        os.makedirs("data/backup", exist_ok=True)

        # Create backup before overwriting existing files
        if os.path.exists("data/books.json"):
            shutil.copy(
                "data/books.json",
                "data/backup/books_backup.json"
            )

        if os.path.exists("data/members.json"):
            shutil.copy(
                "data/members.json",
                "data/backup/members_backup.json"
            )

        # Convert Book objects into dictionaries
        books_data = []

        for book in self.books.values():
            books_data.append(book.to_dict())

        # Save books
        with open("data/books.json", "w") as file:
            json.dump(
                books_data,
                file,
                indent=4
            )

        # Convert Member objects
        members_data = []

        for member in self.members.values():
            members_data.append(member.to_dict())

        # Save members
        with open("data/members.json", "w") as file:
            json.dump(
                members_data,
                file,
                indent=4
            )   


        # ==========================================================
    # LOAD DATA
    # ==========================================================

    def load_data(self):
        """
        Load previously saved data.
        """

        # -------------------------------
        # Load Books
        # -------------------------------

        try:

            if os.path.exists("data/books.json"):

                with open("data/books.json", "r") as file:

                    books = json.load(file)

                    for item in books:

                        book = Book.from_dict(item)

                        self.books[book.isbn] = book

        except Exception as error:

            print(f"Error loading books: {error}")

        # -------------------------------
        # Load Members
        # -------------------------------

        try:

            if os.path.exists("data/members.json"):

                with open("data/members.json", "r") as file:

                    members = json.load(file)

                    for item in members:

                        member = Member.from_dict(item)

                        self.members[member.member_id] = member

        except Exception as error:

            print(f"Error loading members: {error}")


