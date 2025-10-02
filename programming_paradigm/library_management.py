#!/usr/bin/env python3
"""
File: library_management.py
Description: Implements the Book and Library classes for a simple library management system.
"""

class Book:
    """
    Represents a single book in the library.
    """
    def __init__(self, title, author):
        """
        Initializes a Book instance.

        Args:
            title (str): The title of the book (public attribute).
            author (str): The author of the book (public attribute).
        """
        self.title = title
        self.author = author
        # Private attribute (by convention) to track availability
        # True means checked out (unavailable), False means available
        self._is_checked_out = False

    def check_out(self):
        """
        Marks the book as checked out (unavailable).
        """
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False # Already checked out

    def return_book(self):
        """
        Marks the book as returned (available).
        """
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False # Was not checked out

    def is_available(self):
        """
        Returns True if the book is available (not checked out), False otherwise.
        """
        return not self._is_checked_out

    def __str__(self):
        """
        Returns a user-friendly string representation of the book.
        """
        return f"{self.title} by {self.author}"


class Library:
    """
    Manages a collection of Book objects.
    """
    def __init__(self):
        """
        Initializes the Library with an empty list to store books.
        """
        # Private list (by convention) to store Book objects
        self._books = []

    def add_book(self, book):
        """
        Adds a Book instance to the library's collection.

        Args:
            book (Book): An instance of the Book class.
        """
        if isinstance(book, Book):
            self._books.append(book)
            # print(f"Added: {book.title}") # Optional: for verbose output

    def check_out_book(self, title):
        """
        Finds a book by title and marks it as checked out if available.

        Args:
            title (str): The title of the book to check out.
        """
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"Successfully checked out: {title}")
                else:
                    print(f"'{title}' is already checked out.")
                return
        print(f"Error: Book '{title}' not found in the library.")

    def return_book(self, title):
        """
        Finds a book by title and marks it as returned if it was checked out.

        Args:
            title (str): The title of the book to return.
        """
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"Successfully returned: {title}")
                else:
                    print(f"'{title}' was not checked out.")
                return
        print(f"Error: Book '{title}' not found in the library.")

    def list_available_books(self):
        """
        Prints the title and author of all books that are not checked out.
        """
        available_count = 0
        for book in self._books:
            if book.is_available():
                print(book)
                available_count += 1
        
        if available_count == 0 and len(self._books) > 0:
            print("No books are currently available.")
        elif len(self._books) == 0:
             print("The library is empty.")

# --- The main.py code is for testing and should be run separately ---
from library_management import Book, Library

def main():
    # Setup a small library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    # Initial list of available books
    print("Available books after setup:")
    library.list_available_books()

    # Simulate checking out a book
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    # Simulate returning a book
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()

if __name__ == "__main__":
    main()