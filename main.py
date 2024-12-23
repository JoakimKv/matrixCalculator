
# Imports the MainMenu class (that in turn imports the Program class) to be
# used in our main python file.

from mainmenu import MainMenu

# Create an instance of the MainMenu class and then call the method
# startMenu() in the class that starts the program with showing the
# menu with the alternatives for the choices for calculating or setting
# values on the matrix A (and other alternatives). Note that the MainMenu
# class mostly shows the menus and the Program class makes most of the
# calculations and executions of the code (as reading from and writing to
# a file).

# Create a MainMenu instance.
newMainMenu = MainMenu()

# Call the startMenu() method in the MainMenu class.
newMainMenu.startMenu()
