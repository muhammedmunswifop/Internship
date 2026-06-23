"""3. Library Book Tracking System
"""
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print(f"Title: {self.title}, Author: {self.author}")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"{book.title} added to the library.")

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"{title} removed from the library.")
                return
        print("Book not found.")

    def display_books(self):
            print("Library Books:")
            for book in self.books:
                book.display()


library = Library()

book1 = Book("Python Basics", "John Smith")
book2 = Book("Data Structures", "Alice Brown")

library.add_book(book1)
library.add_book(book2)

library.display_books()

library.remove_book("Python Basics")

library.display_books()