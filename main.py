from fastapi import FastAPI

from web import borrowings as borrow_web
from web import books as books_web
from web import returns as returns_web

app = FastAPI()
app.include_router(borrow_web.router)
app.include_router(books_web.router)
app.include_router(returns_web.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host='0.0.0.0', reload=True)
