"""38.Create a Book class with title and author attributes. Add a method to display book details."""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_details(self):
        print("Title:", self.title)
        print("Author:", self.author)


book1 = Book("The Alchemist", "Paulo Coelho")
book2 = Book("Wings of Fire", "A.P.J. Abdul Kalam")

book1.display_details()
print()
book2.display_details()
