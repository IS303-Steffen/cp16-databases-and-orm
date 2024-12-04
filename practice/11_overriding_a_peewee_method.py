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

# ==========================
# OVERRIDING A PEEWEE METHOD
# ==========================

'''
OVERVIEW
--------
You should remember that when you used inheritance with your own custom classes,
you could override a method that was originally defined in the super class.

When using peewee, we can override some of its methods, such as .create(),
to add some extra functionality.

'''

# 1. **KWARGS, KEY WORD ARGUMENTS
# Make a function called kwargs_example. Make it have a parameter called
# **kwargs, with the two asterisks before it. The function should just print out
# kwargs. Call the function and give it the argument of text="hello" and run it.
# Try running it with more arguments and see what happens.



# 2. **KWARGS EXAMPLE 2
# Make a function called kwargs_example_2 with **kwargs as its only parameter
# Use .get() on kwargs to see if it has a "name" keyword. If it does, make it
# uppercase, put the uppercased version back into kwargs, and then print out
# kwargs



# 3. CREATING A CUSTOMER
# Using the code provided below, create a customer, but make their email
# invalid, like "blablabla". This should work.

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

Customer.create(name="Priya", email="blabla", birth_year=2000, state="CA")


'''
STRUCTURE FOR OVERRIDING .create()
----------------------------------
Because .create() doesn't need an object to run, it is a special method called
a class method. To get this to work, you need to add a "decorator" of 
@classmethod before the method name. Decorators alter or extend the default
behavior of functions


@classmethod
def create(cls, **query):
    # your logic here

    # make sure you use super() to call the original
    return super().create(**query)

'''

# 4. OVERRIDE .create() TO ADD VALIDATION
# Override .create() in your Customer class. Add functionality that only calls
# the super version .create() if "@" is present in the email. If it isn't there
# then just print out a message that says, "A valid email must be provided"
# After adding the functionality, check if your code above still adds a new row


'''
TIP:
----
In a more complex implementation, you might want to raise an exception instead
of just printing out a message. You might also want to use something like 
regular expressions to validate the email instead of just checking for an "@"

'''