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

# ==============================
# USING FOREIGN KEYS WITH PEEWEE
# ==============================

'''
OVERVIEW
--------
In a database, foreign keys are IDs that refer to the primary key of another
table. For example, if a Customer has a primary key of customer_id, that 
customer_id might also appear in an order table so that we can associate
specific orders with a specific customer.

Peewee makes working with foreign keys pretty convenient.

Structure:
field_name = ForeignKeyField(Customer, backref='appointments', on_delete='CASCADE')

'''

# 1. CREATE CLASSES FOR books.db
# Using the existing books.db database, create classes for Author and Book

from peewee import *

# Connect to the SQLite database
db = SqliteDatabase('books.db')

# Define the Peewee models
class BaseModel(Model):
    class Meta:
        database = db

class Author(BaseModel):
    author_id = IntegerField(primary_key=True)
    name = TextField(null=False)
    birth_year = IntegerField(null=False)

class Book(BaseModel):
    book_id = IntegerField(primary_key=True)
    title = TextField(null=False)
    pages = IntegerField(null=False)
    year_published = IntegerField(null=False)
    author_id = ForeignKeyField(Author, backref='books', on_delete="CASCADE")


db.connect()
db.create_tables([Author, Book])

# 2. READ FROM THE DATABASE
# Print out the titles of all the books.

all_books = Book.select()

for book_obj in all_books:
    print((book_obj.title))

'''
Foreign Key Field Structure
---------------------------
field_name = ForeignKeyField(Customer, backref='appointments', on_delete='CASCADE')
'''

# 3. ADDING A FOREIGNKEYFIELD
# In the Book class, make author_id a ForeignKeyField
# Now print out the books, and their author's name


# 4. ACCESSING THROUGH BACK REFERENCE
# Ask the user for an Author's ID. Get that author, print out their data, and
# then print out the title of every book they've written.