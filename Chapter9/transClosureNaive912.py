# Chapter 9, Computer Project 12: Given the matrix representing a relation on a 
# finite set, find the matrix representing the transitive closure of this relation 
# by computing the join of the Boolean powers of the matrix representing the relation.
# A Procedure for Computing the Transitive Closure(R*)
# procedure transitive closure (MR : zero–one n × n matrix) * denotes bool product
#   A := MR
#   B := A
#   for i := 2 to n
#       A := A * MR
#       B := B ∨ A
#   return B{B is the zero–one matrix for R*}

from copy import deepcopy
from DiscreteMathRosen.Chapter2.booleanproduct211 import booleanproduct
from DiscreteMathRosen.Chapter9.transitive93 import transitive


def main():
    # Input
    inputMatrix = [[1,0,1,0],[0,1,0,1],[0,0,0,0],[1,1,0,0]]
    # Output
    output = transClosure(inputMatrix)

    print(f"Test Matrix: {inputMatrix}")
    print(f"Transitive Closure(TC) of Test Matrix: {output}")
    print(f"Is Test Matrix Transitive:{transitive(inputMatrix)}. Is TC transitive:{transitive(output)}.")




def transClosure(inputMatrix):
    oneMat = deepcopy(inputMatrix)
    twoMat = deepcopy(oneMat)
    n = len(inputMatrix)
    for i in range(2,n + 1):
        oneMat = booleanproduct(oneMat, inputMatrix)
        twoMat = join(oneMat, twoMat)
    return twoMat


def join(oneMat, twoMat):
    firstMatrix = deepcopy(oneMat)
    secondMatrix = deepcopy(twoMat)
    n = len(oneMat)
    resultMatrix = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            if (firstMatrix[i][j] == 1) or (secondMatrix[i][j] == 1):
                resultMatrix[i][j] = 1
    return resultMatrix


if __name__ == "__main__":
    main()