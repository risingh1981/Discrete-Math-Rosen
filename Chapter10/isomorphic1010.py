# Chapter 10, Computer Project 10: Given the lists of edges of two simple undirected graphs 
# with no more than six vertices, determine whether the graphs are isomorphic.
# Math Foundation: A graph G is isomorphic to graph H is there is a bijection alpha from the
# vertices of G to the vertices of H which preserves adjacency and non-adjacency. Every 
# bijection of a set onto itself gives a permutation, and any permutation gives rise to a bijective 
# function.
# So we generate a permutation of the vertices in G and generate the permutation matrix for
# this permutation and also the transpose of the permutation matrix.
# Ag = Adj Matrix of G, Ah = Adj Matrix of H, P = Permutation matrix, Pt = transpose of P
# G is isomorphic to H iff  Ag = P*Ah*Pt
# 
from DiscreteMathRosen.Chapter10.graphVertices101 import degree
from DiscreteMathRosen.Chapter10.mGraphColoring import graphColoring
from DiscreteMathRosen.Chapter10.matrixReader2 import read78
from DiscreteMathRosen.Chapter10.edgeGenerator105 import checkSymmetric, edgeGenerator
from DiscreteMathRosen.Chapter10.adjMatrix104 import adjMatrixGenerator
from DiscreteMathRosen.Chapter10.graphVertices101 import degree
from itertools import permutations
import numpy as np
from time import perf_counter_ns
from copy import copy
from DiscreteMathRosen.Chapter10.matrixReader2 import printMatrix


def main():
    
    # Input Edges
    edges1 = [(1, 2), (1,3),(2, 3), (2, 5), (3, 4), (3, 5), (4, 5)]
    edges2 = [(1, 2), (1, 3), (1, 4), (2, 3), (3, 4), (4, 5)]
    # Convert edges to adjacency matrices.
    '''
    adjMatrix1 = adjMatrixGenerator(edges1) # True indicates undirected graph
    adjMatrix2 = adjMatrixGenerator(edges2)
    key1 ="Case z"
    key2 = "Case z"
    
    print(f"Output of call to isomorphic in Main(): {isomorphic(adjMatrix1,adjMatrix2, key1, key2)}.")
    '''
    # Use graphs from sample instead
    n = 4 # read78 will load n = 4 adjacency matrices into dict graphs
    graphs = read78(n)
    count = 0
 
    for key in graphs:
        if (count == 0):
            key1 = key
            count += 1
        elif (count == 1):
            key2 = key
            count = 0
            print(f"Graphs {key1} and {key2} are isomorphic: {isomorphic(graphs[key1],graphs[key2])}")
    '''
    TIMING RESULTS:
    About to start checking permutations for graph with 10 vertices. Time for initial check=0.0001204 seconds.
    PC bijectionFound1:(1, 4, 2, 5, 10, 3, 6, 8, 7, 9). Time: 4.6631647 seconds
    PCEM bijectionFound4:(1, 4, 2, 5, 10, 3, 6, 8, 7, 9). Time: 0.0942607 seconds
    Graphs 10.1 and 10.2 are isomorphic: (1, 4, 2, 5, 10, 3, 6, 8, 7, 9)
    About to start checking permutations for graph with 12 vertices. Time for initial check=0.0002228 seconds.        
    PC0 bijectionFound1:(1, 3, 6, 11, 8, 9, 12, 10, 7, 4, 2, 5). Time: 410.6566237 seconds
    PCEM bijectionFound1:(1, 3, 6, 11, 8, 9, 12, 10, 7, 4, 2, 5). Time: 8.4342 seconds
    Graphs 12.1 and 12.2 are isomorphic: (1, 3, 6, 11, 8, 9, 12, 10, 7, 4, 2, 5)    
    '''
    

def isomorphic(adjMatrix1,adjMatrix2, symmetric = True):
    start = perf_counter_ns()
    # Extract edges
    edges1 = edgeGenerator(adjMatrix1)
    edges2 = edgeGenerator(adjMatrix2)
    # Rule out if difference in number of edges
    if (len(edges1) != len(edges2)):
        return False
    # Rule out if different sequences of degree for vertices or different number 
    # of vertices.
    vDict1, slovList1 = sortedListOfVertDegrees(edges1)
    vDict2, slovList2 = sortedListOfVertDegrees(edges2)
    
    if (slovList1) != (slovList2):
        return False
    
    # So far we know, the 2 graphs have same number of vertices, edges and degree sequences.
    # Next, we generate permutations sequetially of vertices in Matrix and discard the
    # permutation if its not mapping a vertex to one of equal degree
    sortedList1 = sorted(vDict1.keys())
    # Create 2 permutation generators to test each function with.
    permGenerator = permutations(sortedList1)
    permGenerator1 = permutations(sortedList1)
    
    vertexCount = len(sortedList1)
    end = perf_counter_ns()
    print(f"About to start checking permutations for graph with {vertexCount} vertices. Time for initial checks = {(end - start)/ (10 ** 9)} seconds.")
    # Function permChecker uses algorithm checking if Ag = P*Ah*Pt  
    start = perf_counter_ns()
    bijectionFound = permChecker(permGenerator,sortedList1, vDict1, vDict2, adjMatrix1, adjMatrix2)
    end = perf_counter_ns()
    pcTime = end - start
    print(f"PC bijectionFound:{bijectionFound}. Time: {pcTime / (10 ** 9)} seconds")
     
    # PermCheckerWithEdgeMatch,
    start = perf_counter_ns()
    bijectionFound1 = permCheckerWithEdgeMatch(edges1, edges2, permGenerator1,sortedList1, vDict1, vDict2)
    end = perf_counter_ns()
    pcemTime = end - start
    print(f"PCEM bijectionFound1:{bijectionFound1}. Time: {pcemTime / (10 ** 9)} seconds")
    
    return bijectionFound1
   

def permCheckerWithEdgeMatch(edges1, edges2, permGenerator,sortedList1, vDict1, vDict2):
    try:
        bijectionFound = False
        skipCheck = (vDict1 == vDict2)
        while True:
            skipPerm = False
            notFound = False
            nextPerm = next(permGenerator)
            if not skipCheck:
                for index, vertex in enumerate(sortedList1):
                    if vDict1[vertex] != vDict2[nextPerm[index]]:
                        skipPerm = True
                        break
            if skipPerm:
                continue
            for edge in edges1:
                if (nextPerm[edge[0] - 1] <= nextPerm[edge[1] - 1]):
                    if (nextPerm[edge[0] - 1],nextPerm[edge[1] - 1]) in edges2:
                        continue
                    else:
                        notFound = True
                        break
                else:
                    if (nextPerm[edge[1] - 1],nextPerm[edge[0] - 1]) in edges2:
                        continue
                    else:
                        notFound = True
                        break
            if not notFound:
                bijectionFound = nextPerm
                break
        return bijectionFound
    except StopIteration:
        return bijectionFound


def permChecker(permGenerator,sortedList1, vDict1, vDict2, adjMatrix1, adjMatrix2):
    vertexCount = len(sortedList1)
    bijectionFound = False
    skipCheck = (vDict1 == vDict2)
    while True:
        try:
            nextPerm = next(permGenerator)
            skipPerm = False
            # Check if mapping degrees match
            for index, vertex in enumerate(sortedList1):
                if vDict1[vertex] != vDict2[nextPerm[index]]:
                    skipPerm = True
                    break   
            if not skipCheck:
                for index, vertex in enumerate(sortedList1):
                    if vDict1[vertex] != vDict2[nextPerm[index]]:
                        skipPerm = True
                        break
            if skipPerm:
                continue
            # If for loop breaks because perm wasn't matching up vertices with same degree,
            # then reset skipPerm to False and goto next iteration of While look to try next perm 
            if skipPerm:
                skipPerm = False
                continue
            # Generate permutation matrix of current permutation.
            permMatrix = np.zeros((vertexCount,vertexCount), dtype = int)
            for index in range(vertexCount):
                permMatrix[sortedList1[index] - 1][nextPerm[index] - 1] = 1
            # Generate Transpose of Permutation Matrix
            permMatrixTransponse = permMatrix.transpose()
            # Check if Ag = P*Ah*Pt
            if np.array_equal(adjMatrix1, np.dot(np.dot(permMatrix, adjMatrix2),permMatrixTransponse)):
                bijectionFound = nextPerm
                break

        except StopIteration:
            break

    return bijectionFound


# Returns list of degrees for all vertices in increasing order
def sortedListOfVertDegrees(edges):
    valueDict = degree(edges) # Returns dict with keys for each vertex and degrees for values.
    degreeList = list(valueDict.values())
    # Generate a dict of possible degrees as keys and vertices for values.
    degreeDict = {}
    for key,value in valueDict.items():
        if value in degreeDict:
            degreeDict[value].append(key)
        else:
            degreeDict[value] = [key]
    return valueDict, sorted(degreeList)


if __name__ == "__main__":
    main()