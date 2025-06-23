from book import Book

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.checked_out_books = {}

    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("The argument must be an instance of the Book class.")
        self.books.append(book)

    def add_user(self, username):
        if not username:
            raise ValueError("Username must not be empty.")
        self.users.append(username)

    def check_out_book(self, username, book):
        if username not in self.users:
            raise ValueError("User '{}' is not registered.".format(username))
        if not isinstance(book, Book):
            raise TypeError("The argument must be an instance of the Book class.")
        if book not in self.books:
            raise ValueError("Book '{}' by {} is not in the library.".format(book.title, book.author))
        if book.is_checked_out:
            raise ValueError("Book '{}' by {} is already checked out.".format(book.title, book.author))

        self.checked_out_books[username] = book
        book.is_checked_out = True

    def return_book(self, username, book):
        if username not in self.users:
            raise ValueError("User '{}' is not registered.".format(username))
        if not isinstance(book, Book):
            raise TypeError("The argument must be an instance of the Book class.")
        if book not in self.books:
            raise ValueError("Book '{}' by {} is not in the library.".format(book.title, book.author))
        if book not in self.checked_out_books or self.checked_out_books[username] != book:
            raise ValueError("Book '{}' by {} was not checked out by '{}'.".format(book.title, book.author, username))

        self.checked_out_books.pop(username)
        book.is_checked_out = False

    def search_books(self, search_term):
        if not search_term:
            raise ValueError("Search term must not be empty.")
        return [book for book in self.books if search_term.lower() in book.title.lower()]
