class Book:
    def __init__(self, title, author, year):
        #Initialize a Book instance with title, author, and year.
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        #Destructor method that prints a message when a Book instance is deleted.
        print(f"Deleting {self.title}")

    def __str__(self):
        #String representation of the Book instance for human-readable format.
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        #String representation of the Book instance for debugging purposes.
        return f"Book('{self.title}', '{self.author}', {self.year})"
