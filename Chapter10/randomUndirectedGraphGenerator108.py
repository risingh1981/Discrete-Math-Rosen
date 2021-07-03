# Chapter 10, Computer Project 8: Given a positive integer n, generate a simple 
# undirected graph with n vertices by producing an adjacency matrix for the graph
# so that all simple graphs with n vertices are equally likely
# to be generated.
# Simple undirected graph doesn't have loops or multiple edges.
# Algorithm I will use is to number the squares in the adjacency matrix from 1 to n^2.
# I will consider the following set A = {1,2,...,n^2}. The powerset of this set contains
# 2^(n^2) sets. Each set in the powerset represents a possible adjacency matrix
# of a graph. The subsets in the powerset are numbered from 0 to 2^(n^2)-1. The binary
# representation of this number indicates which elements of A will be in the subset.
# For example, if you look at the binary representation of the number 4, which is 100.
# Since there is only one 1 bit in the third position, the third element of set A is the only
# element that is in the subset, thus the adjacency matrix would have a 1 in position number 3
# and 0's everywhere else. By picking a number at random in the range 0 to 2^(n^2)-1, I will
# be picking a random subset from the powerset of A. The subset represents 1 simple graph which
# is equally likely as any other simple graph to be picked.
from random import randint
from math import floor


def main():
    # Input (number of vertices)
    n = 20
    # Output: Function will generate adjacency matrix of a random simple graph.
    answer = generateRandomSimpleGraph(n)
    
    print(answer)
    

    
# Function will return an adjacency matrix for a simple graph such that all simple 
# graphs with n vertices are equally likely to be generated.
def generateRandomSimpleGraph(n):
    squaresInAdjMatrix = (n ** 2) - n # Not counting n squares which represent loops.
                                            # and dividing by two as only counting squares above main diagonal.
    maxSimpleGraphs = 2 ** squaresInAdjMatrix # Max number of loop-less undirected graphs(aka simple)
    # Generate random number from 0 to maxSimpleGraphs - 1:
    randNumber = randint(0,maxSimpleGraphs)
    # Generate simple graph based on binary representation of the number randNumber.
    adjMatrix = createAdjMatrix(randNumber,n)
    # Return adjacency matrix
    return adjMatrix

def createAdjMatrix(randNumber, n):
    onesValues = determineOneValues(randNumber)
    adjMatrix = [([0] * n) for _ in range(n)]
    for val in onesValues:
        index = determineIndex(val, n)
        if index[1] > index[0]: # Only use values that are above main diagonal and reflect them.
            adjMatrix[index[0]][index[1]] = 1
            adjMatrix[index[1]][index[0]] = 1
    return adjMatrix

def determineOneValues(randNumber):
    # Generate the reverse order of binary representation of randNumber
    binNum = bin(randNumber)[::-1]
    onesValues = [(index+1) for index,bin in enumerate(binNum) if bin == "1"]
    return onesValues
     
# If each square is numbered in increasing order from left to right and top to bottom skipping
# over squares (i,j) if i = j, determineIndex returns the index associated with 
# number value of this numbering system.
def determineIndex(val,dim):
    if (val % (dim-1) == 0):   # Value falls in right column of matrix
        row = int(val/(dim-1)) - 1
        if (row != (dim - 1)): # checking if its not the last row
            col = dim - 1
        else:                  # if it is the last row
            col = dim - 2
    else:                      # Val is not in last column
        row = floor(val/(dim-1))
        col = val - ((dim-1)*row) - 1
        if col >= row:         # if col>=row, add one because we are skipping over indices (i,j) where i=j
            col += 1
    return (row,col)


   

if __name__ == "__main__":
    main()