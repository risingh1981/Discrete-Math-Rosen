# Chapter 10, Computer Project 11: Given an adjacency matrix of a graph and a positive 
# integer n, find the number of paths of length n between two vertices. 
# (Produce a version that works for directed and undirected graphs.) Will assume problem
# statement doesn't mean simple paths which is a path that doesn't pass through same vertex more
# than once.
# Math Definitions:
# Path, a sequence of vertices connected by edges, of length zero consists of a single 
# vertex. Circuit = a path that begins and ends at same vertex, in an undirected graph.
# Circuit also called cycle in directed graphs.
# For a graph G (can be directed, undirected, with/without loops/multiple edges), 
# with vertices v1,...,vn, the number of paths of length r from vi to vj is the entry
# in position (i,j) of the adjacency matrix of graph G to the r power(A^r).
import numpy as np

def main():
    # Input
    n = 4
    adjMatrix = [[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]]

    # Output: Paths of length n
    print(paths(adjMatrix, n))


def paths(adjMatrix, n):
    adjMatNP = np.array(adjMatrix)
    pathsMathNP = adjMatNP
    for i in range(n-1):
        pathsMathNP =  np.dot(pathsMathNP,adjMatNP)
    # pathsMathNP = adjMatrix ^ n
    return pathsMathNP


if __name__ == "__main__":
    main()