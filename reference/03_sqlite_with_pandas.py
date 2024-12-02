import sqlite3
import pandas as pd


db = sqlite3.connect('books.db')


df_books = pd.read_sql('select * from book', db, index_col='book_id')

print(df_books)

