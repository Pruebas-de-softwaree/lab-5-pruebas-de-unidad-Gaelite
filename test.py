from library import Library
from book import Book
from user import User

lib = Library()
lib.add_book(Book("1984", "George Orwell", 1949, "ISBN001"))

lib.add_user(User("Anna", "U001"))
lib.add_user(User("Kira", "U002"))

lib.borrow_book("U002", "ISBN001")

# lib.borrow_book("U002", "ISBN001")
