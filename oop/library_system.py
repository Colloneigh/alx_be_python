class Book:
    def __init__(self, title, author):
        #Initialize a Book instance with title and author.
        self.title = title
        self.author = author

    def __str__(self):
        #String representation of the book.
        return f"Book: {self.title} by {self.author}"

# Derived class for EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        #Initialize an EBook instance, extending Book with file_size.
        super().__init__(title, author)  # Initialize title and author from Book class
        self.file_size = file_size  # Initialize file size in KB

    def __str__(self):
        #String representation of the eBook.
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

# Derived class for PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        #Initialize a PrintBook instance, extending Book with page_count.
        super().__init__(title, author)  # Initialize title and author from Book class
        self.page_count = page_count  # Initialize page count

    def __str__(self):
        #String representation of the print book.
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

# Library class to manage a collection of books (Composition)
class Library:
    def __init__(self):
        #Initialize the Library with an empty list of books.
        self.books = []

    def add_book(self, book):
        #Add a book (Book, EBook, or PrintBook) to the library.
        self.books.append(book)

    def list_books(self):
        #Print details of all the books in the library.
        for book in self.books:
            print(book)
