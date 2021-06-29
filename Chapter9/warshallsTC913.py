# Chapter 9, Computer Project 13: Given the matrix representing a relation on a 
# finite set, find the matrix representing the transitive closure of this
# relation using Warshall’s algorithm.
# The Naive Algorithm used in the previous exercise can find the transitive closure 
# of a relation on a set with n elements using 2*n^3*(n−1) bit operations. However,
# the transitive closure can be found by Warshall’s algorithm using only 2*n^3 
# bit operations.
# Warshall Algorithm:
# procedure Warshall (MR : n × n zero–one matrix)
# W : = MR
# for k : = 1 to n
#   for i : = 1 to n
#       for j : = 1 to n
#           wij : = wij ∨ (wik ∧ wkj )
#  return W {W = [wij] is MR*(Trans closure)}

from copy import deepcopy
from DiscreteMathRosen.Chapter9.transitive93 import transitive


def main():
    # Input
    inputMatrix = [[0, 0, 0, 1], [1, 0, 1, 0], [1, 0, 0, 1], [0, 0, 1, 0]]

    # Output
    output = warshalls(inputMatrix)

    print(f"Test Matrix: {inputMatrix}")
    print(f"Transitive Closure(TC) of Test Matrix: {output}")
    print(f"Is Test Matrix Transitive:{transitive(inputMatrix)}. Is TC transitive:{transitive(output)}.")



def warshalls(inputMatrix):
    warshalls = deepcopy(inputMatrix)
    n = len(inputMatrix)
    for w in range(n):
        for row in range(n):
            for col in range(n):
                warshalls[row][col] = 1 if ((warshalls[row][col] == 1) or ((warshalls[row][w] == 1) and (warshalls[w][col] == 1))) else 0
    return warshalls


if __name__ == "__main__":
    main()
