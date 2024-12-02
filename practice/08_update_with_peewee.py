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
# UPDATING WITH PEEWEE - GETTING STUFF OUT OF THE DATABASE
# =======================================================

'''
OVERVIEW
--------
In CRUD, U stands for updating, meaning changing data that already
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


# 1. UPDATING USING .save()
# Get customer with the id of 3. Run get_info on them. Change their birth_year
# to be 2010, then call .save() on the customer object. Check if the change
# is in the database.


'''
You can also update multuiple records using .update

e.g.
Student.update({Student.age: 25}).where(Student.age < 21).execute()
'''