
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.borrowed = False
    def borrow(self):
        if self.borrowed == False:
            self.borrowed = True
            print(self.title, "has been borrowed.")
        else:
            print(self.title, "is already borrowed.")
    def return_book(self):
        if self.borrowed == True:
            self.borrowed = False
            print(self.title, "has been returned.")
        else:
            print(self.title, "was not borrowed.")
class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
        print(book.title, "added to library.")
    def display_books(self):
        print("\nLibrary Books:")
        for book in self.books:
            if book.borrowed:
                status = "Borrowed"
            else:
                status = "Available"
            print("Title:", book.title)
            print("Author:", book.author)
            print("ISBN:", book.isbn)
            print("Status:", status)
            print()
library = Library()
book1 = Book("Python Programming", "Guido", "101")
book2 = Book("Java Basics", "James", "102")
library.add_book(book1)
library.add_book(book2)
library.display_books()
print("\nBorrowing a book...")
book1.borrow()
library.display_books()
print("\nReturning the book...")
book1.return_book()
library.display_books()

Has simple if-else conditions, making it easy to understand and write in exams.
