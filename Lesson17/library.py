from typing import List


class Author:

    def __init__(self, name: str, birthday: int, books: List):
        self.name = name
        self.birthday = birthday
        self.books = books

    def __str__(self):
        return f"Name: {self.name}, birthday: {self.birthday}, books: {self.books}"

    def __repr__(self):
        return f"object <class Author> name: {self.name}, birthday: {self.birthday}, books: {self.books}"


class Book:
    def __init__(self, name: str, year: int, author: Author):
        self.name = name
        self.year = year
        self.author = author

    def __str__(self):
        return f"Book {self.name} written in {self.year} by {self.author}"

    def __repr__(self):
        return f"object <class Book> name: {self.name}, year: {self.year}, author: {self.author}"


class Library:
    books: List[Book] = []

    def __init__(self, name: str):
        self.name = name

    def new_book(self, name: str, year: int, author: Author):
        book = Book(name, year, author)
        self.books.append(book)
        return book

    def group_by_author(self, author: Author):
        return list(filter(lambda book: book.author == author, self.books))

    def group_by_year(self, year: int):
        return list(filter(lambda book: book.year == year, self.books))

    def __repr__(self):
        return f"object <class Library> name: {self.name} with books: {self.books}"

    def __str__(self):
        return f"Books: {self.books}"

    def __len__(self):
        return len(self.books)


if __name__ == "__main__":
    library = Library("Lunar Labyrinth Library")
    print(library)
    library.new_book("The House of Mirth by Edith Wharton", 1905, Author("Edith Wharton", 1862,
                                                                         ["The Ghost Stories of Edith Wharton", "Summer", "Ethan Frome"]))
    print(library)