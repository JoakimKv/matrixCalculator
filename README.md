
# "matrixCalculator" Program

By Joakim Kvistholm.

The program can use different operators and calculations on a 3 x 3 matrix A
(or A1). Calculations such as det(A), A^n and exp(A) can be made. To enable this 
calculations the package numpy with the subpackage linalg is especially useful.

The main menu can be seen below.

"Main Menu:"

"1. Insert a new 3 x 3 matrix  A1 (to get a symmetric matrix A = A1.T * A1)"
"2. Calculate eigenvectors and eigenvalues for A"
"3. Show the matrix A on screen"
"4. Calculate the determinant of A"
"5. Calculate A^n (3 <= n <= 10)"
"6. Calculate exp(A)"
"7. Get saved matrix A from file"
"8. Save matrix A to file"
"Q. Quit program"

You can insert a new 3 x 3 matrix A1 that is then transformed to a symmetric
matrix A (Where A = A1.T * A1. A1 is transposed and then multiplied by A1.).
There are some advantages to use symmetric matrices in the calculations. One
advantage is that real eigenvalues are obtained. Another way to obtain the
3 x 3 matrix A is to load it from a file ("savedmatrix.txt"). You can also
save your matrix A to a file ("savedmatrix.txt"). The user can also make the 
choice to see the matrix A on the screen.

All calculations are made on a symmetric 3 x 3 matrix A. Among the matrix calculations 
on the 3 x 3 matrix A you can obtain the eigenvalues v (a vector) and the eigenvectors 
S (a matrix where the columns are the eigenvectors). A^n (3 <= n <= 10), exp(A) and 
det(A) can be calculated. To calculate the scalar det(A) and the matrix A^n the linalg 
subpackage (la) could be used. To calculate the matrix exp(A) I needed to add my own 
calculations to numpy by using the Cayley Hamilton method and "la.inv(B)" method to 
find the inverse of the B matrix. For this solution the eigenvalues needed to be 
compared. For the calculations the subpackage linalg has been very useful and the 
matrix multiplication operator "@".

The program allows a certain amount of user mistakes. Such as wrong inputs or something
goes wrong with reading or writing to a file, when the matrix A is saved or stored.
More fail safes could be used in the program. A better algoritm when comparing
eigenvalues when exp(A) is calculated then abs(lambda_i-lambda_j) >= eps could be used.
To catch more user / program errors (with try ... except [className]) could be used. The 
menu could be made more intuitive with a "pause button" when looking at the results. More
matrix calculations could be made.

One main purpose with the program is to give "extensive" comments to the code.

## Packages

No "pip install" is needed.
Imports numpy and math.


