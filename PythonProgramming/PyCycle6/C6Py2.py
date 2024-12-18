# Base class Publisher
class Publisher:
    def __init__(self, publisher_id, publisher_name):
        self.publisher_id = publisher_id
        self.publisher_name = publisher_name

    def display_publisher_details(self):
        # Method to display publisher details
        print(f"Publisher ID: {self.publisher_id}")
        print(f"Publisher Name: {self.publisher_name}")


# Derived class Book from Publisher
class Book(Publisher):
    def __init__(self, publisher_id, publisher_name, title, author):
        # Initialize Publisher class using super() and add Book-specific attributes
        super().__init__(publisher_id, publisher_name)
        self.title = title
        self.author = author

    def display_book_details(self):
        # Method to display book details
        print(f"\nBook Title: {self.title}")
        print(f"Author: {self.author}")
        # Display publisher details using the parent class method
        self.display_publisher_details()


# Derived class Python from Book
class Python(Book):
    def __init__(self, publisher_id, publisher_name, title, author, price, no_of_pages):
        # Initialize Book class using super() and add Python-specific attributes
        super().__init__(publisher_id, publisher_name, title, author)
        self.price = price
        self.no_of_pages = no_of_pages

    def display_python_details(self):
        # Method to display Python book details, overriding the method in Book class
        print(f"\nPrice: ${self.price}")
        print(f"Number of Pages: {self.no_of_pages}")
        # Display book and publisher details by calling the parent methods
        self.display_book_details()


# Getting the relevant information from the user
publisher_id = input("Enter Publisher ID: ")
publisher_name = input("Enter Publisher Name: ")
title = input("Enter Book Title: ")
author = input("Enter Author Name: ")
price = float(input("Enter Price of the Book: $"))
no_of_pages = int(input("Enter the Number of Pages: "))

# Creating an object of Python (derived class) using user input
python_book = Python(
    publisher_id=publisher_id,
    publisher_name=publisher_name,
    title=title,
    author=author,
    price=price,
    no_of_pages=no_of_pages
)

# Displaying the details of the Python book
python_book.display_python_details()
