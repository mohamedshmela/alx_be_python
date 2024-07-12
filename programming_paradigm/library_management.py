class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False

    def return_book(self):
        pass 

class Library:

    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)
        print(f'Book "{book.title}" added to the library.')

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if not book.is_checked_out:
                    book.is_checked_out = True
                    print(f'Book "{title}" checked out.')
                    return
                else:
                    print(f'Book "{title}" is already checked out.')
                    return
        print(f'Book "{title}" not found in the library.')

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.is_checked_out:
                    book.is_checked_out = False
                    print(f'Book "{title}" returned to the library.')
                    return
                else:
                    print(f'Book "{title}" was not checked out.')
                    return
        print(f'Book "{title}" not found in the library.')

    def list_available_books(self):
        available_books = [book for book in self._books if not book.is_checked_out]
        if not available_books:
            print("No books available in the library.")
        else:
            print("Available books:")
            for book in available_books:
                print(f"- {book.title} by {book.author}")

library = Library()
library.add_book(Book("1948", "george"))
library.list_available_books()