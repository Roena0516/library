from . import con, cur

def enroll_book(title: str, author: str):
    if not title and not author :
        return False

    sql = f"insert into books (title, author) values (?, ?)"
    cur.execute(sql, (title, author))
    con.commit()
    return True

def get_all_books():
    sql = f"select * from books"
    cur.execute(sql)
    books = cur.fetchall()
    return books

def delete_book(book_id):
    sql = f"delete from books where book_id = ?"
    cur.execute(sql, (book_id,))
    con.commit()
    return True

def get_book(book_id):
    sql = f"select * from books where book_id = ?"
    cur.execute(sql, (book_id,))
    book = cur.fetchone()
    return book

def get_book_id(title) :
    sql = f"select book_id from books where title = ?"
    cur.execute(sql, (title,))
    book_id = cur.fetchone()
    return book_id