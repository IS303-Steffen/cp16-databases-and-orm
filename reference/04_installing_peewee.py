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
# INSTALLING PACKAGES WITH PIP
# ============================

import peewee as pd

'''
FIRST:
    Try running this code. You're probably going to get an error.
    This is because peewee is a library that you need to download from the
    internet.

HOW TO DOWNLOAD LIBRARIES:
    Python comes installed with a package/library downloader called pip!

    1. In VS Code, go to Terminal > New Terminal (at the top of the screen)

    2. Then in the bottom Terminal window, type:
                pip install peewee
        and then hit the enter/return key. If that doesen't work, try:
                pip3 install peewee
        then hit the enter/return key
    
    3. Then, try and run this python file again, if it prints out the message
       below, you are good.

    Note: If you prefer, you can also just run pip in the normal terminal
          application on Mac or the command line on Windows (or powershell).
          It doesn't have to be in VS Code.

IT STILL ISN'T WORKING FOR ME:

    1. Most likely, you are installing the package to one version of python,
       and then running a different version in VS Code. You can click the
       numbers at the bottom right of VS Code near where it says "Python" to
       see all the versions of Python that you have installed.

    2.1 For MacOS users:
        In the terminal, type "which pip" or "which pip3" and press return.
        That will show you which version of python pip is installing packages
        to.
    
    2.2 For Windows users:
        Open up the command line NOT in VSCode by typing in "cmd" in the
        Windows search bar and pressing enter. Then type "where pip" or
        "where pip3" to see which version of python pip is installing packages
        to.

    3. Try clicking the numbers near the bottom right of your screen in VS Code
       and then select the version of python that says "Recommended" 
'''

print("If this prints, that means you installed peewee correctly")