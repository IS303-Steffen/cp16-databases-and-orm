import sqlite3

db = sqlite3.connect('books.db')

result = db.execute('select * from book;')

for x in result:
    print(x)