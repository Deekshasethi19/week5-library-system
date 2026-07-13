"""
Unit tests for the Member class.
"""

import unittest
from library_system.member import Member


class TestMember(unittest.TestCase):

    def setUp(self):
        """
        Create a Member object before every test.
        """
        self.member = Member(
            "M001",
            "Dee"
        )

    def test_member_creation(self):

        self.assertEqual(self.member.member_id, "M001")
        self.assertEqual(self.member.name, "Dee")
        self.assertEqual(len(self.member.borrowed_books), 0)

    def test_borrow_book(self):

        success, message = self.member.borrow_book("ISBN001")

        self.assertTrue(success)
        self.assertEqual(len(self.member.borrowed_books), 1)

    def test_return_book(self):

        self.member.borrow_book("ISBN001")

        success, message = self.member.return_book("ISBN001")

        self.assertTrue(success)
        self.assertEqual(len(self.member.borrowed_books), 0)

    def test_can_borrow(self):

        self.assertTrue(self.member.can_borrow())


if __name__ == "__main__":
    unittest.main()