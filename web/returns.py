from fastapi import APIRouter, Body

from service import returns as service
from service import borrowings as borrowings

router = APIRouter(prefix="/return")

@router.post("")
def return_book(borrower: str = Body(...), title: str = Body(...)):
    if not borrower and not title:
        return False

    borrowings.return_borrower_books(borrower)
    return service.return_book(borrower, title)