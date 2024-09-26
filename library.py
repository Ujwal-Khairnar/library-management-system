class Book:
    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False

    def __repr__(self):
        return f"{self.title} by {self.author} ({self.year})"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.is_borrowed:
                    raise Exception("Book is already borrowed")
                book.is_borrowed = True
                return
        raise Exception("Book not found")
    
    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if not book.is_borrowed:
                    raise Exception("Book was not borrowed")
                book.is_borrowed = False
                return
        raise Exception("Book not found")

    def view_available_books(self):
        return [book for book in self.books if not book.is_borrowed]
