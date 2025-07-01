from fastapi import APIRouter, Body

from service import books as service

router = APIRouter(prefix="/books")

@router.post("")
def enroll_book(title: str = Body(...), author: str = Body(...)):
    if not title and not author :
        return False

    return service.enroll_book(title, author)

@router.get("")
def list_books():
    book_list = service.get_available_books()

    return book_list

@router.delete("/{book_id}")
def delete_book(book_id: int):
    if not book_id :
        return False
    return service.delete_book(book_id)