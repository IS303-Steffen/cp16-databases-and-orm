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

# =====================================
# PRACTICE - OVERRIDING A PEEWEE METHOD
# =====================================


# 1. OVERRIDING PRACTICE

'''
Use the same dog database and class that you used in the previous practice:

The dog table should include:
    id
    name
    age
    favorite food (make it so this field is optional by adding null=True)
    
Except now, make it so that
    1. the age must be over 0 and below 25 when you create a dog

    2. the favorite food must be at least 3 characters long if it is present
       But it still should be possible to create a dog with no favorite food.

'''