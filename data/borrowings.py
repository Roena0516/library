from . import con, cur

def borrow(borrower: str, book_id: int):
    sql = f"insert into borrowings (book_id, borrower) values (?, ?)"
    cur.execute(sql, (book_id, borrower))
    con.commit()
    return True

def get_all_borrowings() :
    sql = f"select * from borrowings"
    cur.execute(sql)
    return cur.fetchall()