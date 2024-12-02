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

# ============================
# SQLITE IN PYTHON
# ============================

# 1. Connect to the sqlite database, and use .execute() to get the data from it.


