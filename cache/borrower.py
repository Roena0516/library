import json

from . import redis_client

def save_borrow_book_title(borrower, title):
    cache_key = "borrower:" + borrower + ":books"
    redis_client.set(cache_key, title)
    return True

def get_borrower_books(borrower) :
    cache_key = "borrower:" + borrower + ":books"
    value = redis_client.get(cache_key)
    return json.loads(value)