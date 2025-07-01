from data import borrowings as data
from data import books as books
from cache import borrower as cache

def borrow(borrower, title) :
    if not borrower and not title :
        return False

    book_id = books.get_book_id(title)

    if book_id :
        cache.save_borrow_book_title(borrower, title)
        return data.borrow(borrower, book_id)

    return False

def get_month_books(borrow_month) :
    borrowings = data.get_all_borrowings()
    print(borrowings)
    borrow_list = []
    for borrow in borrowings :
        print(int(borrow[3][5:7]))
        if int(borrow[3][5:7]) == borrow_month :
            book = books.get_book(borrow[1])
            borrow_dict = {
                "borrower": borrow[2],
                "title": book[1],
                "author": book[2]
            }
            borrow_list.append(borrow_dict)

    return borrow_list

def get_borrower_books(borrower) :
    titles = cache.get_borrower_books(borrower)
    print(titles)
    title_dict = {
        "borrower": borrower,
    }
    book_list = []
    for title in titles :
        book_list.append(title)
    title_dict["books"] = book_list
    return title_dict

def return_borrower_books(borrower) :
    if borrower :
        return cache.return_borrower_books(borrower)
    else :
        return None