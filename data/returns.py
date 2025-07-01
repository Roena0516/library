import datetime

from . import con, cur

def return_book(borrower, book_id) :
    sql = f"update borrowings set returned_at = ? where book_id = ? and borrower = ?"
    cur.execute(sql, (datetime.datetime.now(), book_id, borrower))
    con.commit()
    return True