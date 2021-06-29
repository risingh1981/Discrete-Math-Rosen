# Chapter 9, Computer Project 11: Given the matrix representing a relation on a 
# finite set, find the matrix representing the symmetric closure of this relation.
from copy import deepcopy
from DiscreteMathRosen.Chapter9.symmetric92 import symmetric

def main():
    # Input
    A = [[1,0,1,0],[0,1,0,1],[0,0,0,0],[1,1,0,0]]
    # Output
    output = symmetricClosure(A)

    print(f"Test Matrix: {A}")
    print(f"Symmetric Closure(SC) of Test Matrix: {output}")
    print(f"Is Test Matrix Symmetric:{symmetric(A)}. Is SC symmetric:{symmetric(output)}.")



def symmetricClosure(A):
    scRel = deepcopy(A)
    dim = len(scRel)
    for i in range(dim):
        for j in range(dim):
            if (scRel[i][j] == 1):
                scRel[j][i]= 1

    return scRel


if __name__ == "__main__":
    main()