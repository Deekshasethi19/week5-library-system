"""
main.py

This is the entry point of the Library Management System.

The user interacts with the program through a menu-driven interface.
"""

# Import Library class
from library import Library


def display_menu():
    """
    Display all available options.
    """

    print("\n" + "=" * 60)
    print("        LIBRARY MANAGEMENT SYSTEM")
    print("=" * 60)

    print("1. Add Book")
    print("2. Remove Book")
    print("3. Register Member")
    print("4. Remove Member")
    print("5. Borrow Book")
    print("6. Return Book")
    print("7. Search Book")
    print("8. Display All Books")
    print("9. Display All Members")
    print("10. Library Statistics")
    print("11. Save Data")
    print("12. Load Data")
    print("0. Exit")

    print("=" * 60)


def search_menu():
    """
    Display search options.
    """

    print("\nSearch Book By")
    print("1. Title")
    print("2. Author")
    print("3. ISBN")


def main():

    # Create Library object
    library = Library()

    # Load previously saved data (if available)
    library.load_data()

    while True:

        display_menu()

        choice = input("\nEnter your choice: ")

        # =====================================================
        # ADD BOOK
        # =====================================================

        if choice == "1":

            print("\nAdd New Book")

            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            year = input("Publication Year: ")

            success, message = library.add_book(
                title,
                author,
                isbn,
                year
            )

            print(message)

        # =====================================================
        # REMOVE BOOK
        # =====================================================

        elif choice == "2":

            isbn = input("Enter ISBN: ")

            success, message = library.remove_book(isbn)

            print(message)

        # =====================================================
        # REGISTER MEMBER
        # =====================================================

        elif choice == "3":

            member_id = input("Member ID: ")
            name = input("Member Name: ")

            success, message = library.register_member(
                member_id,
                name
            )

            print(message)

        # =====================================================
        # REMOVE MEMBER
        # =====================================================

        elif choice == "4":

            member_id = input("Member ID: ")

            success, message = library.remove_member(
                member_id
            )

            print(message)

        # =====================================================
        # BORROW BOOK
        # =====================================================

        elif choice == "5":

            member_id = input("Member ID: ")
            isbn = input("Book ISBN: ")

            success, message = library.borrow_book(
                member_id,
                isbn
            )

            print(message)

        # =====================================================
        # RETURN BOOK
        # =====================================================

        elif choice == "6":

            member_id = input("Member ID: ")
            isbn = input("Book ISBN: ")

            success, message = library.return_book(
                member_id,
                isbn
            )

            print(message)

        # =====================================================
        # SEARCH BOOK
        # =====================================================

        elif choice == "7":

            search_menu()

            option = input("Choose an option: ")

            if option == "1":

                keyword = input("Enter Title: ")

                books = library.search_by_title(keyword)

                if books:
                    for book in books:
                        print(book)
                else:
                    print("No matching books found.")

            elif option == "2":

                keyword = input("Enter Author: ")

                books = library.search_by_author(keyword)

                if books:
                    for book in books:
                        print(book)
                else:
                    print("No matching books found.")

            elif option == "3":

                isbn = input("Enter ISBN: ")

                book = library.search_by_isbn(isbn)

                if book:
                    print(book)
                else:
                    print("Book not found.")

            else:
                print("Invalid search option.")

        # =====================================================
        # DISPLAY ALL BOOKS
        # =====================================================

        elif choice == "8":

            library.display_books()

        # =====================================================
        # DISPLAY ALL MEMBERS
        # =====================================================

        elif choice == "9":

            library.display_members()

        # =====================================================
        # LIBRARY STATISTICS
        # =====================================================

        elif choice == "10":

            stats = library.get_statistics()

            print()

            for key, value in stats.items():
                print(f"{key}: {value}")

        # =====================================================
        # SAVE DATA
        # =====================================================

        elif choice == "11":

            library.save_data()

            print("Data saved successfully.")

        # =====================================================
        # LOAD DATA
        # =====================================================

        elif choice == "12":

            library.load_data()

            print("Data loaded successfully.")

        # =====================================================
        # EXIT
        # =====================================================

        elif choice == "0":

            save = input(
                "\nDo you want to save before exiting? (Y/N): "
            ).strip().lower()

            if save == "y":
                library.save_data()

            print("\nThank you for using Library Management System.")

            break

        else:

            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()