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

# =======================================================
# READING WITH PEEWEE - GETTING STUFF OUT OF THE DATABASE
# =======================================================

'''
OVERVIEW
--------
In CRUD, R stands for reading, meaning reading (or getting) data that already
exists out of your database.


'''


# Setup provided for you:
from peewee import *

db = SqliteDatabase('customers.db')

class Customer(Model):
    id_customer = AutoField(primary_key=True)
    name = CharField()
    email = CharField()
    birth_year = IntegerField()
    state = CharField()

    class Meta:
        database = db
    
    def get_info(self):
        return f"Customer {self.id_customer}'s data: Name: {self.name} | Email: {self.email} | Birth Year: {self.birth_year} | State: {self.state}"

db.connect()
db.create_tables([Customer])

customers = [
    {"name": "Alice", "email": "alice@example.com", "birth_year": 1990, "state": "CA"},
    {"name": "Bob", "email": "bob@example.com", "birth_year": 1985, "state": "NY"},
    {"name": "Charlie", "email": "charlie@example.com", "birth_year": 1978, "state": "TX"},
    {"name": "Diana", "email": "diana@example.com", "birth_year": 1992, "state": "FL"},
    {"name": "Ethan", "email": "ethan@example.com", "birth_year": 1980, "state": "WA"},
    {"name": "Fiona", "email": "fiona@example.com", "birth_year": 1995, "state": "OR"},
    {"name": "George", "email": "george@example.com", "birth_year": 1988, "state": "NV"},
    {"name": "Hannah", "email": "hannah@example.com", "birth_year": 1991, "state": "PA"},
    {"name": "Ian", "email": "ian@example.com", "birth_year": 1983, "state": "IL"},
    {"name": "Jane", "email": "jane@example.com", "birth_year": 1975, "state": "AZ"},
]

# 1. SET UP DATA
# To save time, uncomment the code below, run the code, and then comment the
# code again (so you don't create duplicate rows each time you run this)

#Customer.insert_many(customers).execute()

# 2. GET ALL ROWS FROM THE DATABASE
# Use Customer.select() to get all the customers in your database. Then loop
# through them and print out their name and birth year

list_of_customers = Customer.select()

for customer_obj in list_of_customers:
    print(f"{customer_obj.name} {customer_obj.birth_year}")

# 3. EXTEND YOUR CUSTOMER CLASS
# In your customer class, write a method called `get_info` that returns a
# string like this:
# Customer 1's data: Name: John | Email: example@gmail.com | Birth Year: 2000 | State: Utah
# then call that method on each of the customers in your table.

for customer_obj in list_of_customers:
    print(f"{customer_obj.get_info()}")

print()

# 4. GET A SUBSET OF THE DATA
# Using .where() after .select() Get only those customers born after 1990

filtered_customers = Customer.select().where(Customer.birth_year > 1990)
for customer_obj in filtered_customers:
    print(customer_obj.get_info())
print()


# 4. GET A SUBSET OF THE DATA WITH MULTIPLE CONDITIONS
# Using .where() after .select() Get only those customers born after 1990 and
# from Pennsylvania (PA). In peewee, you need to put each condition in
# parentheses, with `&` instead of `and`. (| is used instead of or. ~ is used
# instead of not).

filtered_customers = Customer.select().where((Customer.birth_year > 1990) & (Customer.state == "PA"))
for customer_obj in filtered_customers:
    print(customer_obj.get_info())


# 5. GET A SINGLE RECORD USING .get
# This will give you an error if it can't find exactly 1 row in the database
# Best used with ids (primary keys). Get customer with the id of 3 and print
# out their name

customer_3 = Customer.get(Customer.id_customer == 3)

print()
print(customer_3.name)


'''
Other methods:

.get
.get_or_none
.raw
'''