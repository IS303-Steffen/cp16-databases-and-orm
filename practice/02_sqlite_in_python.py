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

# ================
# SQLITE IN PYTHON
# ================

# 1. Import the books.db datbase by importing the sqlite3 library and using the
# .connect function. Then use .execute() to get the data from it. Loop through
# the result and print out each row.


