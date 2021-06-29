# Chapter 9, Computer Project 10: Given the matrix representing a relation on a 
# finite set, find the matrix representing the reflexive closure of this
# relation.
from DiscreteMathRosen.Chapter9.reflexive91 import reflexive
from copy import deepcopy

def main():
    # Input
    A = [[1,0,1,1],[0,1,0,1],[1,0,0,0],[1,1,0,0]]
    # Output
    output = reflexiveClosure(A)

    print(f"Test Matrix: {A}")
    print(f"Reflexive Closure(RC) of Test Matrix: {output}")
    print(f"Is Test Matrix Reflexive:{reflexive(A)}. Is RC reflexive:{reflexive(output)}.")

def reflexiveClosure(inputMatrix):
    rcMatrix = deepcopy(inputMatrix)
    for i in range(len(rcMatrix)):
        rcMatrix[i][i] = 1
    return rcMatrix

if __name__ == "__main__":
    main()