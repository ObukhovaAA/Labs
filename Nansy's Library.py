class Library:
    
    def __init__(self, name, books = None):
        if books == None:
            books = [[]]
        self.books = books
        self.name = name


    def __add__(self, book):
        if len(self.books[0]) == 0:
            self.books.pop(0)    
        self.books = self.books + book.info
        return self.books 


    def __str__(self):
        return (f'{self.books}')

class Book:
    
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year
        self.info = [[book.name, book.author, str(book.year)]]

biblio = Library(name = "Nansy's Library")

book = Book(
    name = "Lalala. Part 1",
    author = "Nansy",
    year = 2000
)

newbook = Book(
    name = "Lalala. Part 2",
    author = "Nansy",
    year = 2021
)

biblio = biblio + newbook
biblio = biblio + book
print(biblio)
