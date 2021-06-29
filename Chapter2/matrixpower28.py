# Chapter 2, Computer Project 8: Given a square matrix A and a positive integer p, find A^p.
# Import matrix multiplication function from previous exercise.
from DiscreteMathRosen.Chapter2.matrixmulti27 import matrixproduct

def main():
    # Input: Enter a square(nxn) matrix(A) and the power(p) you want to take of that matrix.
    p = 5 
    A = [[1,2,3],[4,5,6],[7,8,9]]

    # Call function matrixpower(A, p)
    print(matrixpower(A, p))

def matrixpower(A,p):
    B = A
    for i in range(0,p-1):
        B = matrixproduct(A,B)
    return B



if __name__ == "__main__":
    main()




