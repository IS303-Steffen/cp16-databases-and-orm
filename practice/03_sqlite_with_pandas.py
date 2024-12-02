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
# SQLITE WITH PANDAS
# ============================

import sqlite3
import pandas as pd


db = sqlite3.connect('books.db')

# 1. Given the above connection, get a dataframe of the whole book table

