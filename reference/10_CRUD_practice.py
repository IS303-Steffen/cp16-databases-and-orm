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
# CRUD PRACTICE WITH PEEWEE
# =========================

# 1. Create a dog database
'''
Create a database for dogs usingi peewee

The dog table should include an id, name, age and favorite food.

Using peewee
    1. create a few dogs
    2. print out some of their info,
    2. update a dog's data
    3. delete a dog
'''