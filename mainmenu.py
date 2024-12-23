
# Imports Program class to be used to make calculations on the
# matrix A and other executions of code as reading and writing
# to file.
from program import Program

# Create the class MainMenu.
class MainMenu:

    # This is the constructor to the MainMenu class. Create an instance of the Program class
    # to be used in the MainMenu class. The input parameter "self" is used to reference
    # "objects" (methods and variables) in the class.
    def __init__(self):

        # An instance ("self.myProgram") of the Program class is created. The
        # constructor for the Program class will be called.
        self.myProgram = Program()

    # The "startMenu(self)" method in the MainMenu class. Here the menu of
    # choices are created and displayed. The input parameter self is needed
    # and used within the MainMenu class.
    def startMenu(self):

        # Setting the boolean variable run to True.
        run = True

        # Using a while loop to repeat the choices until the user
        # chooses to quit the program with "q", which makes run is False,
        # which ends the while loop. The variable run = True when the
        # program starts so that the menu will be displayed at least once when
        # the program starts.
        while run:

            # Writes out the choices and reads answer from the screen and stores the
            # answer in the "answer" variable. The strip() function removes
            # starting and ending blanks in the answer (which is a text). The "f" in
            # f"Text {var1}" formats the string, which is not necessary to use here (since
            # no variables in the code below). print(f"{var1}") writes out the value for the
            # variable var1 on the screen. print("\n") writes out a new line on the screen.
            answer = input(f"\nMain menu:\n"
                           "\n1. Insert a new 3 x 3 matrix  A1 (to get a symmetric matrix A = A1.T * A1)"
                           "\n2. Calculate eigenvectors and eigenvalues for A"
                           "\n3. Show the matrix A on screen"
                           "\n4. Calculate the determinant of A"
                           "\n5. Calculate A^n (3 <= n <= 10)"
                           "\n6. Calculate exp(A)"
                           "\n7. Get saved matrix A from file"
                           "\n8. Save matrix A to file"
                           "\nQ. Quit program"
                           "\n\n-> ").strip()

            # The "match ... case" syntax is used to pick out the specific choices
            # for the answer variable. It is similar to "if" syntax but for more specific
            # choices based on a variable, here "answer". The function "lower()" converts
            # the answer to lower case letters.
            match answer.lower():

                # The first choice "1" in "answer". Here the user can input the matrix A1
                # (3 x 3). Then the program creates a symmetric matrix A (3 x 3) from A1.
                # Both A1 and A is then printed to the screen. The code
                # "self.myProgram.readMatrixA()" executes statements in the Program class
                # that reads and gets values for A1 to create A. Most of the code to execute
                # things are in the Program class except the menu and some print statements.
                # Note that print("...") prints to the screen. The "self.myProgram" is an
                # instance of the Program class that is used in the MainMenu class. The
                # "readMatrixA()" is a method in the Program class (who reads A1 and creates
                # A).
                case "1":
                    print("\nInsert a new 3 x 3 matrix A1 (to get a symmetric A = A1.T * A1)\n")
                    self.myProgram.readMatrixA()

                # Choice "2" in "answer". The "self.myProgram.calcEigenValAndVect()" method
                # in the Program class that calculates the eigenvectors v and the eigenvalues
                # S (the columns in S) for the matrix A. Then v and S is printed to the screen.
                # Note that we have two outputs from the method (function).
                case "2":
                    print("\nCalculate eigenvectors and eigenvalues for A")
                    v, S = self.myProgram.calcEigenValAndVect()
                    print(f"Eigenvalues:\n {v} \n")
                    print(f"Eigenvectors (columns):\n {S} \n")

                # Choice "3" in "answer". Prints the matrix A on the screen.
                case "3":
                    print("\nShow the matrix A on screen")
                    print(self.myProgram.A)

                # Choice "4" in "answer". The "self.myProgram.calcDetOfMatrixA()" method
                # in the Program class that calculates the determinant det(A) to the matrix A.
                # Then det(A), which is a scalar, is printed to the screen.
                case "4":
                    print("\nCalculate the determinant of A")
                    detA = self.myProgram.calcDetOfMatrixA()
                    print(f"The determinant of A is: {detA}\n\n")

                # Choice "5" in "answer". The "self.myProgram.calcAPowerNAndPrint()" method
                # in the Program class calculates A^n to the matrix A.
                # The user will first choose a value for n (3 <= n <= 10) and then A^n
                # is calculated and printed to the screen.
                case "5":
                    print("\nCalculate A^n (3 <= n <= 10)")
                    self.myProgram.calcAPowerNAndPrint()

                # Choice "6" in "answer". The "self.myProgram.calcExpAAndPrint()" method
                # in the Program class calculates exp(A) to the matrix A.
                # The Cayley Hamilton method in mathematics is used.
                # The matrix exp(A) is calculated and printed to the screen.
                case "6":
                    print("\nCalculate exp(A)")
                    self.myProgram.calcExpAAndPrint()

                # Choice "7" in "answer". The "self.myProgram.getSavedMatrixFromFile()" method
                # in the Program class loads the symmetric matrix A (3 x 3) from file.
                case "7":
                    print("\nGet saved matrix A from file")
                    self.myProgram.getSavedMatrixFromFile()

                # Choice "7" in "answer". The "self.myProgram.saveMatrixToFile()" method
                # in the Program class saves the symmetric matrix A (3 x 3) to file. You
                # must either have loaded a matrix A from file or inputted values into A1
                # in choice "1" in the menu to save a matrix (as matrix A).
                case "8":
                    print("\nSave matrix A to file")
                    self.myProgram.saveMatrixToFile()

                # Choice "q" in "answer". Quits the program by setting run = False, which also
                # ends the while loop and therefore the program.
                case "q":
                    run = False
                    print("\nQuiting program!")

                # Choice "_" = "default" = {none of the above choices} in "answer". Displays
                # an error message and returns to displaying the menu.
                case _:
                    print(f"\nYou wrote '{answer}'\nYou need to choose one of 1, 2, 3, 4, 5, 6, 7, 8 or Q!")
