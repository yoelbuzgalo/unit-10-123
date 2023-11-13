import library

def test_book_const():
    # Setup
    author = "Toni Morrison"
    title = "Beloved"
    copies = 1

    # Invoke
    book = library.Book(title, author, copies)

    # Analysis
    assert book.author == author
    assert book.title == title
    assert book.copies == copies
