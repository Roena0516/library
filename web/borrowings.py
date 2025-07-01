from fastapi import APIRouter, Body
from service import borrowings as service

router = APIRouter(prefix="/borrows")

@router.post("")
def borrow(borrower: str = Body(...), title: str = Body(...)):
    if not borrower and not title :
        return False

    return service.borrow(borrower, title)

@router.get("/month/{borrow_month}")
def get_month_books(borrow_month: int):
    if not borrow_month :
        return {"Error": "Borrowing month not found"}

    return service.get_month_books(borrow_month)

@router.get("{borrower}/books")
def get_books(borrower: str):
    if not borrower :
        return {"Error": "Borrowing books not found"}
    return service.get_borrower_books(borrower)