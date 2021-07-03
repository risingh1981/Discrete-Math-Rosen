# Chapter 10, Computer Project 9: Given a positive integer n, generate a simple directed
# graph with n vertices by producing an adjacency matrix for the graph so that all simple 
# directed graphs with n vertices are equally likely to be generated.
# Simple = No loops or multiple edges.

from random import randint
from math import floor

def main():
    # Input value of n:
    n = 4
    
    # Output:
    print(generateRandomSimpleGraph(n))




    
# Function will return an adjacency matrix for a simple graph such that all simple 
# graphs with n vertices are equally likely to be generated.
def generateRandomSimpleGraph(n):
    squaresInAdjMatrix = (n ** 2) - n # Not counting n squares which represent loops.
    maxSimpleGraphs = 2 ** squaresInAdjMatrix # Max number of loop-less graphs(aka simple)
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
        adjMatrix[index[0]][index[1]] = 1
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