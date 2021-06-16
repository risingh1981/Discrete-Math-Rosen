# Chapter 2, Computer Project 12: Given a square Boolean matrix A and a positive integer n,
# find A[n].
# Import function from previous exercise which calculcates boolean product of 2 0/1 Matrices
from booleanproduct211 import booleanproduct

def main():
    # Input: Original boolean matrix and power of matrix desired.
    power = 3
    A = [[0,0,1],
         [1,0,0],
         [1,1,0]]
    # Output
    # Variable Ap is the result of matrix A taken to pth power. Variable unitat is the power of A that 
    # results in the unit matrix, or None if no power upto the value of power variable results in a unit matrix.
    Ap, unitat = boolpower(A, power)
    print(f"Matrix A = {A}.")
    print(f"A^{power} = {Ap}")
    if (unitat != None):
        print(f"A becomes unit matrix at power of {unitat}.")



# Function boolpower(A,p) takes as Input: 1) A is a boolean matrix 2)p is the power of matrix A you desire.
# Function boolpower(A,p) Returns 2 values. First value is A^p. Second value is the power at which A becomes
# a unit matrix, or None if no power upto p results in a unit matrix.
def boolpower(matrix, power):
    dim = len(matrix)
    unitMatrix = [[1 for x in range(dim)] for y in range(dim)]
    unitat = 1 # Variable to store power at which the matrix equals the unit matrix, so no successive powers 
               # need to be taken. As a unit matrixs boolean product with any boolean matrix is the unit matrix. 
    # Checking to see if original matrix is unitmatrix. No powers need to be taken if it is
    if (matrix == unitMatrix):
        return matrix, unitat
    resultMatrix = matrix
    for i in range(power-1):
        print(f"In loop for calculating powers. i ={i}")
        resultMatrix = booleanproduct(matrix,resultMatrix)
        if (resultMatrix == unitMatrix):
            unitat = i + 2
            return resultMatrix, unitat

    return resultMatrix, None

if __name__ == "__main__":
    main()