import csv

class Book:
    __slots__ = ['title', 'author', 'copies']
    def __init__(self, title, author, copies=1):
        self.title = title
        self.author = author
        self.copies = copies

class Patron:
    __slots__ = ['name', 'id', 'want_list', 'has_list']
    def __init__(self, name, id, wants=[], has=[]):
        self.name = name
        self.id = id

        if wants == None:
            self.wants = set()
        else:
            self.wants = wants

        if has == None:
            self.has = set()
        else:
            self.has = has

class Library:
    __slots__ = ['shelves', 'title_catalog', 'author_catalog']
    def __init__ (self,filename):
        self.shelves = list()
        self.title_catalog = dict()
        self.author_catalog = dict()
        with open(filename) as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)
            for record in csv_reader:
                title, author, copies = record
                book = Book(title, author, int(copies))
                self.shelves.append(book)
                self.title_catalog[book.title] = book
                if author not in self.author_catalog:
                    self.author_catalog[book.author] = set()
                self.author_catalog[book.author].add(book)
                
            

def main():
    book = Book("Dune", "Frank Herbert", 3)
    print(book.title, book.author, book.copies)

    library = Library("data/books.csv")
    books = library.author_catalog["George Orwell"]
    for book in books:
        print(book.title)

if __name__ == "__main__":
    main()