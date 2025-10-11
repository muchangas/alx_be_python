class Book:
    """
    A class to represent a book with attributes for title, author, and publication year.
    It includes magic methods for construction, destruction, and string representations.
    """

    def __init__(self, title, author, year):
        """
        Constructor: Initializes a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor: Called when the object is about to be destroyed (garbage collected).
        Prints a message indicating the book being deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        String Representation (__str__): Returns a user-friendly string for the book.
        Used by the built-in 'print()' function.

        Returns:
            str: The book's details in the format "(title) by (author), published in (year)".
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official Representation (__repr__): Returns a string that can be used to
        recreate the object. Used by the built-in 'repr()' function.

        Returns:
            str: A string in the format f"Book('{self.title}', '{self.author}', {self.year})".
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"

from book_class import Book

def main():
    # Creating an instance of Book
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrating the __str__ method
    print(my_book)  # Expected to use __str__

    # Demonstrating the __repr__ method
    print(repr(my_book))  # Expected to use __repr__

    # Deleting a book instance to trigger __del__
    del my_book

if __name__ == "__main__":
    main()