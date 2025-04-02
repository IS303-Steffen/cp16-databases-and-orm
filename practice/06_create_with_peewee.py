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

# =========================================
# CREATING WITH PEEWEE - ORM MODEL AND ROWS
# =========================================

'''
OVERVIEW
--------
The main point of using something like peewee is that is has pre-built code
for constructing classes that correspond to tables in your database. This is
called an ORM model. We will create a database, an ORM model, and a row in the
database on this file.

BASIC IDEA
----------
    1. You create a class for each table, with variables for each column
       Columns are often called "fields"
    
    2. Each instance/object of your class corresponds to a row in your database


A big part of this is just becoming familiar with peewee's syntax. But once
you get the basic idea down, you can apply this this any other ORM you might
learn in the future.
'''


'''
IS from library import * OK?
---------------
Generally, you shouldn't just import everything all at once from a library.
However, since you'll be using so many things from peewee, in this case
it is more justifiable.
'''


# 1. IMPORT EVERYTHING FROM PEEWEE
# Use the syntax: from peewee import *
# This will give you access to everything inside of the peewee library without
# needing to type out peewee. before everything.



# 2. CREATE YOUR DATABASE CONNECTION
# Connect to your database. In this case, we'll create a new one called
# customers.db



# 3. CREATE YOUR ORM MODEL FOR THE CUSTOMER TABLE
# Create a Customer class. This will need to inherit from peewee's class Base.
# You want your customer table to have the following fields (columns), so they
# need to be included in your class:
#   id_customer: AutoField(primary_key=True)
#   name: CharField
#   email: CharField
#   birth_year: IntegerField
#   state: CharField


'''
RULES FOR peewee MODELS
-----------------------
1. Your class must inherit from peewee's Model class

2. Every column (field) in your table needs a corresponding class variable, set
   equal to one of peewee's field types. Here are the most common ones you
   might use:
        CharField() - for strings
        TextField() - for really long strings (like entire blog posts, etc.)
        IntegerField() - for integers
        FloatField() -  for floats
        BooleanField() - for booleans
        AutoField() - for primary keys. Creates an integer that automatically
                      increments by one for each new thing

3. Inside of your class, you need ANOTHER class called `Meta` with a class
   variable called `database` set equal to your database connection object
'''


# 4. CONNECT TO YOUR DATABASE AND CREATE THE CUSTOMER TABLE
# Using the database connection object you made in step 2, connect (or the
# first time you run your code, create it) by calling .connect()
# Afterwards, call the .create_tables method. Give it a list, with the Customer
# class inside of it.



# 5. CREATE A CUSTOMER USING Customer.create()
# Make a row in your Customer database using Customer.create(). You need to
# provide the field names and the values for that field (e.g. name="John") for
# each field. Store the result in a variable, and then try printing out the
# name of the object that it gave you.


'''
What if you want to insert many rows at once?
---------------------------------------------

You can use Customer.insert_many([dictionaries for each row]).execute()

You could also do stuff with pandas_df.to_sql()
'''