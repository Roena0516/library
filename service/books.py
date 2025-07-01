import service
from data import books as data
# from cache import books as cache

def enroll_book(title, author):
    if not title and not author :
        return False

    return data.enroll_book(title, author)

def get_available_books():
    books = data.get_all_books()
    print(books)
    book_list = []
    for book in books:
        print(book)
        book_dict = {
            "title": book[1],
            "author": book[2],
        }
        if book[3] == 1:
            book_list.append(book_dict)

    return book_list

def get_book(book_id):
    book = data.get_book(book_id)
    return book

def delete_book(book_id):
    if not book_id :
        return False
    book = get_book(book_id)
    if book[3] == 1 :
        result = data.delete_book(book_id)
        return result
    return False