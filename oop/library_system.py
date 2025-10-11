# --- Inheritance: Base Class ---
class Book:
    """
    The base class for all books in the library.
    It includes the standard __str__ method for representation.
    """
    def __init__(self, title, author):
        """Initializes a Book instance."""
        self.title = title
        self.author = author

    def __str__(self):
        """Returns the user-friendly string representation of the Book."""
        return f"Book: {self.title} by {self.author}"

# --- Inheritance: Derived Classes ---

class EBook(Book):
    """
    Represents an electronic book, inheriting from Book.
    """
    def __init__(self, title, author, file_size):
        """Initializes an EBook instance."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """
        Overrides the base __str__ method to include EBook-specific details.
        """
        # Call the base __str__ to get common details, then replace "Book" with "EBook"
        base_str = super().__str__().replace("Book", "EBook")
        return f"{base_str}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """
    Represents a physical printed book, inheriting from Book.
    """
    def __init__(self, title, author, page_count):
        """Initializes a PrintBook instance."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """
        Overrides the base __str__ method to include PrintBook-specific details.
        """
        # Call the base __str__ to get common details, then replace "Book" with "PrintBook"
        base_str = super().__str__().replace("Book", "PrintBook")
        return f"{base_str}, Page Count: {self.page_count}"


# --- Composition: Library Class ---
class Library:
    """
    A class that manages a collection of books, demonstrating composition.
    """
    def __init__(self):
        """Initializes a Library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Adds a Book (or derived class) instance to the library's collection."""
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print(f"Error: {book} is not a valid book type.")

    def list_books(self):
        """
        Prints the details of every book in the library.
        This now implicitly calls the __str__ method on each book object.
        """
        for book in self.books:
            print(book)

from library_system import Book, EBook, PrintBook, Library

def main():
    # Create a Library instance
    my_library = Library()

    # Create instances of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books in the library
    my_library.list_books()

if __name__ == "__main__":
    main()