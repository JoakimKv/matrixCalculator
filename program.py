
# Imports the numpy package as np (for instance for np.zeros()) and the
# special part of this package "linalg" as la to be used in the Program
# class (for instance for matrix calculations).

# The package math is also included to calculate for instance
# exp(x).

import numpy as np
from numpy import linalg as la
import math


# Create the class Program.
class Program:

    # The constructor for the Program class. "self" references the
    # class methods or variables and is an input variable to all methods
    # in the class.
    def __init__(self):

        # The "self." in the variable names is only a syntactic reference in the names
        # to point out that the variables are class variables (belongs to the class).

        # The matrix A is set to 3 x 3 zero matrix (in the class variable "self.A").
        self.A = np.zeros((3, 3))

        # The matrix An (A^n) is set to 3 x 3 zero matrix (in the class variable "self.An").
        self.An = np.zeros((3, 3))

        # The matrix exp(A) is set to 3 x 3 zero matrix (in the class variable "self.expA").
        self.expA = np.zeros((3, 3))

        # Boolean class variable "self.bMatrixAIsSet" (or "bMatrixAIsSet") in the class
        # is initially set to False.
        self.bMatrixAIsSet = False

        # The "self.fileName" has the filename "savedmatrix.txt". The matrix A is stored
        # in this file or loaded from this file.
        self.fileName = "savedmatrix.txt"

    # Checks if the datatype of the text can be converted to a float and returns a boolean,
    # with the value True if it can be converted and False if it can not be converted.
    # The input to the function is a text (num). The input parameter "self" needs to be
    # included in all class methods.
    def isfloat(self, num):

        # Use a "try ... except ValueError" statement (ValueError: an "error" class
        # for datatype). The method tries to convert the text value num to a float, if
        # it can with no "errors" (no compilation problems) it returns True, otherwise
        # False.
        try:
            float(num)
            return True
        except ValueError:
            return False

    # Checks if the datatype of the text can be converted to a int and returns a boolean,
    # with the value True if it can be converted and False if it can not be converted.
    # The input to the function is a text (num). The input parameter "self" needs to be
    # included in all class methods.
    def isint(self, num):

        # Use a "try ... except ValueError" statement (ValueError: an "error" class
        # for datatype). The method tries to convert the text value num to an int, if
        # it can with no "errors" (no compilation problems) it returns True, otherwise
        # False.
        try:
            int(num)
            return True
        except ValueError:
            return False

    # A class method used in readMatrixA() that handles incorrect input when
    # reading values for the matrix A.
    def handleWrongData(self):

        # Check if the user want to try again to create the matrix A1 and consequently A.
        # The answer is in "txtAnswer" as a text. "strip()" removes starting and ending blanks.
        # "lower()" converts the text to lower case.
        txtAnswer = input("Invalid input. Do you want to try to insert new values again (y/n)?: ").strip()

        # The "if ... else" checks if the answer = "y" (in txtAnswer) then it calls the method
        # readMatrixA() in this class and restarts reading values for the matrix, else a 3 x 3
        # zero matrix is returned (as an indication that something went wrong). Note that
        # readMatrixA() returns the 3 x 3 matrix A if all goes well. "np.zeros()" is used
        # from the numpy package (as np, see the import statement).
        if txtAnswer.lower() == "y":
            return self.readMatrixA()
        else:
            return np.zeros((3, 3))

    # This class method reads a 3 x 3 matrix A1 and creates a symmetric matrix A as
    # A = A.T @ A.
    def readMatrixA(self):

        # while loop to run until you have correctly inserted the matrix A1 or
        # quit the attempt with incorrect values.
        run = True
        while run:
            # For 3 x 3 matrix A1. Read three rows as ("1, 2, 3.2" new line: Three times).
            # The for loop: "for row in range(3)" - loops it three times with the row
            # getting the values "0, 1, 2".
            for row in range(3):
                # Read the first row as text in the variable strRow. "strip()" removes
                # starting and ending blanks. Writes out the variable "{row + 1}" with
                # the values "1, 2, 3".
                strRow = input(f"Three values separated with comma as i.e. 1.2, 2, 3.2 in A for "
                               f"row nr {row + 1}: ").strip()

                # Split the values in strRow to float values as text in strRowNrs.
                # We should have three values.
                strRowNrs = strRow.split(",")

                # Check if wrong input data (empty string: "not strRowNrs") or
                # that we do not have three values ("len(strRowNrs) != 3").
                # If this happens return and call our error handler handleWrongData()
                # that restarts reading A1 (calls readMatrixA() again) or stops reading A1
                # and returns 3 x 3 zero matrix.
                if not strRowNrs or len(strRowNrs) != 3:
                    return self.handleWrongData()

                # Use a for loop as above "for col in range(3)", but with variable
                # col instead of row (loops three times).
                for col in range(3):
                    # Use our class function "isfloat()" to check that the input values
                    # are floats.
                    if self.isfloat(strRowNrs[col]):
                        # Insert the values in our matrix A (A1) if the values are floats.
                        self.A[row][col] = float(strRowNrs[col])
                    else:
                        # If wrong input use our error function in the return statement.
                        # Note that our error function returns a 3 x 3 matrix.
                        return self.handleWrongData()

                # All is OK. End the while loop by setting run = False.
                run = False

                # Mark that we know have a correct A1 (A) matrix.
                self.bMatrixAIsSet = True

        # Print the A1 matrix.
        print(f"\nThe matrix A1 is given by:\n\n")
        print(self.A)

        # Make A = A1.T * A1 a symmetric matrix.
        self.A = self.A.T @ self.A

        # Print the A matrix.
        print(f"The symmetric matrix A = A1.T * A1 is given by:\n\n")
        print(self.A)

        # Return the A matrix (the class variable self.A).
        return self.A

    # A class method calcDetOfMatrixA() that calculates the determinant
    # of the matrix A, det(A), by using numpy package linalg (as la).
    def calcDetOfMatrixA(self):

        # Calculates det(A) to the variable "detA".
        detA = la.det(self.A)

        # Returns this value, detA, from the method (function).
        return detA

    # The class method calcEigenValAndVect() in this class (Program) calculates the
    # eigenvectors v and the eigenvalues S (the columns in S) for the matrix A. "self"
    # is a needed input parameter for the class.
    def calcEigenValAndVect(self):

        # Calculates the eigenvalues and eigenvectors to the 3 x 3 matrix A by
        # using the "eig" function in numpy (linalg) package (as la). It returns
        # two output values v (vector) and S (matrix).
        v, S = la.eig(self.A)

        # Returns two output values v (vector) and S (matrix).
        return v, S

    # A class method used in calcAPowerNAndPrint() that handles incorrect input when
    # reading values for the integer value n (3 <= n <= 10) in the calculation of A^n.
    def handleWrongDataForN(self):

        # Check if the user want to try again to input a new n value when calculating A^n.
        # The answer is in "txtAnswer" as a text. "strip()" removes starting and ending blanks.
        # "lower()" converts the text to lower case.
        txtAnswer = input("Invalid input. Do you want to try to insert new values again (y/n)?: ").strip()

        # The "if ... else" checks if the answer = "y" (in txtAnswer) then it calls the method
        # calcAPowerNAndPrint() in this class and restarts reading values for n and calculating A^n,
        # else a zero matrix is returned (as an indication that something went wrong). Note that
        # calcAPowerNAndPrint() returns the 3 x 3 matrix A^n if all goes well.
        if txtAnswer.lower() == "y":
            return self.calcAPowerNAndPrint()
        else:
            return np.zeros((3, 3))

    # The class method "calcAPowerNAndPrint()" calculates A^n (by using
    # "la.matrix_power(self.A, n)") in the numpy package. Where 3 <= n <= 10.
    # The method prints out and returns A^n.
    def calcAPowerNAndPrint(self):

        # A while loop to read n (3 <= n <= 10).
        run = True
        while run:
            # Read n as text. "strip()" removes starting and ending blanks.
            strAnswer = input("Enter n for A^n (3 <= n <= 10): ").strip()

            # Check if the indata text can be converted to an int by using
            # the class function "isint(strAnswer)".
            if not self.isint(strAnswer):
                # End the while loop by setting run = False.
                run = False

                # Use and return the error handling class function
                # "handleWrongDataForN()". If wrong and user chooses to quit, it returns
                # a 3 x 3 zero matrix else it calls "calcAPowerNAndPrint()" and
                # restarts this method with reading n, calculating A^n and printing
                # and returning this value (A^n).
                return self.handleWrongDataForN()
            else:
                # Now n is an int. Convert the text in strAnswer to an int n.
                n = int(strAnswer)

                # If the int n is 3 <= n <= 10, then calculate A^n, else
                # stop the while loop by setting run = False and call and return
                # the error handler "handleWrongDataForN()".
                if 3 <= n <= 10:
                    run = False

                    # Calculates A^n and store this value in "self.An".
                    self.An = la.matrix_power(self.A, n)

                    # Print the matrix A^n.
                    print(f"The matrix A^n with n = {n} is given by:\n\n")
                    print(self.An)

                    # Return A^n.
                    return self.An
                else:
                    # End the while loop by setting run = False.
                    run = False

                    # Use and return the error handling class function
                    # "handleWrongDataForN()". If wrong and user chooses to quit, it returns
                    # a 3 x 3 zero matrix else it calls "calcAPowerNAndPrint()" and
                    # restarts this method with reading n, calculating A^n and printing
                    # and returning this value (A^n).
                    return self.handleWrongDataForN()

    # The class method "calcExpAAndPrintCalculates()" calculates exp(A) (by using eig
    # in numpy and the Cayley Hamilton method) and prints out exp(A) on screen and
    # returns exp(A) from the function.
    def calcExpAAndPrint(self):

        # Checks if the matrix A is set, if not end this method.
        if not self.bMatrixAIsSet:
            print("Must first set values on the matrix A!")
            return

        # Sets the differance between two values that we count as being zero, for
        # instance eps = 10^(-17). It worked better to set this value to zero in
        # this code, but should normally be set to a value.
        eps = 0

        # Calculate eigenvalues v and eigenvectors S. In this method we only need
        # the eigenvalues v.
        v, S = la.eig(self.A)

        # Three eigenvalues are the same => f(lam_i) = p(lam_i), f'(lam_i) = p'(lam_i),
        # and f''(lam_i) = p''(lam_i). f(x) = exp(x) and p(x) = c0 + c1 * x + c2 * x^2.
        # f(A) = p(A).

        # g does not change because f'(x) = d/dx(exp(x)) = exp(x). Create g.
        g = np.array([math.exp(v[0]), math.exp(v[1]), math.exp(v[2])]).T

        # Check if all three eigenvalues are the same. Create corresponding
        # matrix B (to the equations). Using the Cayley Hamilton method. Create B.
        # Note that abs(v[1]-v[0]) takes the absolute value of the difference v[1]-v[0]
        # which should be less or equal to eps, that is set above for all differences.
        if abs(v[1]-v[0]) <= eps and abs(v[2]-v[1]) <= eps:
            B = np.array([[1, v[0], v[0]*v[0]],
                          [0, 1, 2*v[0]],
                          [0, 0, 2]])

        # (Case 1) Two eigenvalues are the same (three cases) => f(lam_i1) = p(lam_i1),
        # f'(lam_i1) = p'(lam_i1), and f(lam_i2) = p(lam_i2). f(x) = exp(x) and
        # p(x) = c0 + c1 * x + c2 * x^2. f(A) = p(A). Using the Cayley Hamilton method.
        # Create B.
        elif abs(v[1]-v[0]) <= eps:
            B = np.array([[1, v[0], v[0]*v[0]],
                          [0, 1, 2*v[0]],
                          [1, v[2], v[2]*v[2]]])

        # (Case 2) Two eigenvalues are the same. Create B.
        elif abs(v[2] - v[1]) <= eps:
            B = np.array([[1, v[0], v[0] * v[0]],
                         [1, v[1], v[1] * v[1]],
                         [0, 1, 2 * v[1]]])

        # (Case 3) Two eigenvalues are the same. Create B.
        elif abs(v[2] - v[0]) <= eps:
            B = np.array([[1, v[0], v[0] * v[0]],
                         [1, v[1], v[1] * v[1]],
                         [0, 1, 2 * v[0]]])

        # All eigenvalues are different. f(lam_i) = p(lam_i). Create B.
        else:
            B = np.array([[1, v[0], v[0] * v[0]],
                         [1, v[1], v[1] * v[1]],
                         [1, v[2], v[2] * v[2]]])

        # B * ci = g => ci = inv(B) * g and
        # f(A) = exp(A) = p(A) = c0 * I + c1 * A + c2 * A * A.

        # Solve for the coefficients in ci.
        ci = la.inv(B) @ g

        # Calculate exp(A) from ci and I, A, A * A. I = "np.eye(3)" from numpy package.
        # The "@" is used for matrix multiplication.
        self.expA = ci[0] * np.eye(3) + ci[1] * self.A + ci[2] * self.A @ self.A

        # Print the result of exp(A) on screen.
        print("The matrix exp(A) is: \n")
        print(self.expA)

        # Return the result of exp(A)
        return self.expA

    # The class method "getSavedMatrixFromFile()" retrieves a saved
    # matrix A from the file "savedmatrix.txt".
    def getSavedMatrixFromFile(self):

        # Use "try ... except" to catch all errors with reading from file,
        # so that the program do not crash if something goes wrong here.
        # One could split up the "try ... exception [Class name]" for different
        # types of errors to get a better understanding what went wrong, when the
        # program was used. A general error handling works good enough for this program.
        try:

            # Open the file "self.fileName" (= "savedmatrix.txt") for reading.
            # rawMatrix is a file object.
            rawMatrix = open(self.fileName)

            # Reads the whole file as text.
            strRawMatrix = rawMatrix.read()

            # Split the file in its rows (by "\n": new line). Can be a
            # last empty row. Should be three rows.
            strRawMatrixRows = strRawMatrix.split("\n")

            # Use a three times for loop ("for in range(...)"). Outer loop (rows).
            # len(...) checks number of elements in the list (vector).
            # min(a, b) finds the minimum. It should be at most three rows
            # in the for loop ("for i in range(...)"). The rows are "i".
            for i in range(min(len(strRawMatrixRows), 3)):

                # Split on "," (in strRawMatrixRows[i]) to get the column values as text in
                # a list. strRawMatrixNrs contains three values in a "row" (list).
                strRawMatrixNrs = strRawMatrixRows[i].split(",")

                # Use a three times for loop ("for in range(...)"). Inner loop (columns).
                # Convert the values to floats and insert the three values
                # in the matrix A as self.A[row][col] (= self.A[i][j] = a float value). The
                # columns are "j". A is a 3 x 3 matrix.
                for j in range(min(len(strRawMatrixNrs), 3)):
                    self.A[i][j] = float(strRawMatrixNrs[j])

            # Print out to the screen that the matrix is saved.
            print("The matrix A is now obtained from file")

            # Close the file for reading (which is important to make the program "safe").
            rawMatrix.close()

            # Set a marker that a correct matrix A is obtained by using
            # the boolean class variable "self.bMatrixAIsSet" (= True).
            self.bMatrixAIsSet = True

        # Error handling.
        except:

            # Something went wrong with the file reading, print this to screen.
            print("Something went wrong with reading the matrix A from file. Try again!")

    # The class method "getSavedMatrixFromFile()" saves
    # matrix A to the file "savedmatrix.txt".
    def saveMatrixToFile(self):

        # Checks if a correct matrix A exists (is inserted by choice "1"
        # or read from file). If not correct matrix A, print error message and
        # return (end this function).
        if not self.bMatrixAIsSet:
            print("Must first set values on the matrix A before writing to file!")
            return

        # Use "try ... except" to catch all errors with writing to file,
        # so that the program do not crash if something goes wrong here.
        # One could split up the "try ... exception [Class name]" for different
        # types of errors to get a better understanding what went wrong, when the
        # program was used. A general error handling works good enough for this program.
        try:

            # An empty text in strText.
            strText = ""

            # Write the matrix as text row for row (three rows) end with new line "\n".
            # Each row has three columns. A ("self.A") is a 3 x 3 matrix (A[row][col]).
            # All indexes starts at zero (0), "i = 0, 1, 2". A for loop for three
            # iterations. strText will contain three rows (with 3 x 3 floating values).
            for i in range(3):
                strText += f"{self.A[i][0]}, {self.A[i][1]}, {self.A[i][2]}\n"

            # Open the file "self.fileName" (= "savedmatrix.txt") for writing, use
            # the flag "w+" for overwriting the file. rawMatrix is a file object.
            rawMatrix = open(self.fileName, "w+")

            # Write the entire text in strText (the matrix A) to the file.
            rawMatrix.write(strText)

            # Print a message on the screen that the file is saved.
            print("The matrix A is now saved to file")

            # Close the file.
            rawMatrix.close()

        # Error handling.
        except:

            # Something went wrong with the file writing, print this to screen.
            print("Something went wrong with writing the matrix A to file. Try again!")
