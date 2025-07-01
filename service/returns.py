import service
from data import returns as data
from data import books as books

def return_book(borrower: str, title: str) :
    if not borrower and not title :
        return False

    book_id = books.get_book_id(title)

    return data.return_book(borrower, book_id)