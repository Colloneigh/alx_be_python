class Book:
    """A class representing a book with a title, author, and check-out status."""

    def _init_(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track if the book is checked out

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as available (not checked out)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available for checkout."""
        return not self._is_checked_out


class Library:
    """A class representing a library that manages a collection of books."""

    def _init_(self):
        self._books = []  # Private list to store instances of Book

    def add_book(self, book):
        """Add a book to the library collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Mark a book as checked out if available."""
        for book in self._books:
            if book.title == title and book.is_available():
                if book.check_out():
                    print(f"'{title}' has been checked out.")
                    return
        print(f"'{title}' is either not available or already checked out.")

        def return_book(self, title):
            """Return a book to the library, making it available again."""
        for book in self._books:
            if book.title == title and not book.is_available():
                if book.return_book():
                    print(f"'{title}' has been returned.")
                    return
        print(f"'{title}' was not checked out or does not exist in the library.")

    def list_available_books(self):
        """List all books that are currently available for checkout."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")