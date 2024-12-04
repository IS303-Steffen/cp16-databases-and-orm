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
# PRACTICE - USING FOREIGN KEYS WITH PEEWEE
# ==============================

# 1. Adding a foreign key field
'''
Using the Customer class that you've already written previously,
add an Order Class. Orders should have
    - an id
    - item_name
    - quantity
    - a foreign key that corresponds to Customers

Try hardcoding some new orders in. After that, try getting user inputs
to get specific customers and create orders for them.
'''


