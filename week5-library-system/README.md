# 📚 Library Management System

A simple command-line based Library Management System developed using Python and Object-Oriented Programming (OOP).

This project allows users to manage books and members, issue and return books, search records, and store library data using JSON files.

---

## 🚀 Features

- Add new books
- Remove books
- Register library members
- Remove members
- Borrow books
- Return books
- Search books by:
  - Title
  - Author
  - ISBN
- View all books
- View all members
- View library statistics
- Detect overdue books
- Save data into JSON files
- Load saved data
- Automatic data backup
- Menu-driven command line interface

---

## 🛠️ Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- JSON
- File Handling
- Datetime Module
- Unittest

---

## 📂 Project Structure

```
week5-library-system/
│
├── library_system/
│   ├── __init__.py
│   ├── book.py
│   ├── member.py
│   ├── library.py
│   └── main.py
│
├── data/
│   ├── books.json
│   ├── members.json
│   └── backup/
│
├── tests/
│   ├── test_book.py
│   ├── test_member.py
│   └── test_library.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## ▶️ How to Run

1. Clone the repository.

2. Open the project folder.

3. Run the following command:

```bash
python -m library_system.main
```

---

## 🧪 Running Tests

Run the following command to execute all unit tests:

```bash
python -m unittest discover tests
```

---

## 📌 Future Improvements

- GUI version using Tkinter
- Database support using SQLite/MySQL
- Barcode scanner integration
- Book reservation system
- Fine calculation
- Email notifications

---

## 👨‍💻 Author

Developed as part of a Python Internship Project.