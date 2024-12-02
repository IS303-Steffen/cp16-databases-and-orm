import os
import platform

def clear_screen():
    """
    Clears the terminal screen to make it easier to follow along with code.
    """
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

# =========================
# BASIC QUERIES WITH PEEWEE
# =========================

'''
OVERVIEW
--------
You can connect to SQLite databases using peewee, just like you can using the
python standard sqlite3 library. 

The point of this file is to show that this is still possible, but this isn't
the main point of using an ORM like peewee.
'''


# 1. CONNECT TO SQLITE AND RUN A QUERY
# Use peewee.SqliteDatabase() to connect to the books.db database. Then use the
# .execute_sql() method to get all the data from the `author` table. Print it
# all out.
import peewee

db = peewee.SqliteDatabase('books.db')

result = db.execute_sql('select * from author')

for row in result:
    print(row)