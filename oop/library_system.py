class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size

class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

class Library:
    def __init__(self, books: list = []):
        self.books = books

    def add_book(self, book: Book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            if type(book) is PrintBook:
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            elif type(book) is EBook:
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            else:
                print(f"Book: {book.title} by {book.author}")

