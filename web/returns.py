from fastapi import APIRouter, Body

from service import returns as service

router = APIRouter(prefix="/return")

@router.post("")
def return_book(borrower: str = Body(...), title: str = Body(...)):
    if not borrower and not title:
        return False

    return service.return_book(borrower, title)