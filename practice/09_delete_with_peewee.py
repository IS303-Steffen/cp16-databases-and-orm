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

# ======================================================
# DELETING WITH PEEWEE - DELETING ROWS FROM THE DATABASE
# ======================================================

'''
OVERVIEW
--------
In CRUD, D stands for deleting, meaning getting rid of data that already
exists in your database.

'''

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

# 1. DELETE A ROW
# Get the customer with ID 4. Use .delete_instance() to delete them from the
# database. 



'''
You can also delete multiple rows at once
e.g.

Student.delete().where(Student.age > 23).execute()

'''