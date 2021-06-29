# Chapter 9, Computer Project 3: Given the matrix representing a relation on a 
# finite set, determine whether the relation is transitive.
# Algorithm for Determining Transitivity:
# 1) Transitive if following True :∀i∀j if (A^2[i][j] = 1) then (A[i][j] = 1)
# Time Complexity: O(n^3) because of normal matrix multiplication. Can be lowered
# to O(n^2.7) using Strassens algorithm for matrix multiplication.

from DiscreteMathRosen.Chapter2.matrixpower28 import matrixpower

def main():
    # Input:
    A = [[1,1,0],[1,1,1],[0,0,1]]
    # Output
    print(f"Transitive(A):{transitive(A)}")

def transitive(A):
    dim = len(A)
    # unitAt is the power of A that results in a unit matrix.
    # Not relevant for this problem but function boolpower returns 2 values, the power and unitAt.
    aSquared = matrixpower(A, 2)
    
    # For transitivity, A^2 cannot have a non-zero value in spot that was zero in A.
    for i in range(dim):
        for j in range(dim):
            if (aSquared[i][j] >= 1) and (A[i][j] == 0):
                return False
    return True


if __name__ == "__main__":
    main()