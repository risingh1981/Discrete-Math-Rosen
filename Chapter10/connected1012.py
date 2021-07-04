# Chapter 10, Computer Project 12: Given the list of edges of a simple graph, determine
# whether it is connected and find the number of connected components if it is not connected.
# An undirected graph is connected is there is a path between every pair of vertices. It has
# 1 connected component, itself.  If it is not connected, then it has >=1 connected components,
# each of which is connected.
# a directed graph is strongly connected if there is a path from a to b and from b to a for all
# pairs of vertices, and weakly connected if there is a path between every pair of vertices
# in its undelying undirected subgraph.
from ast import Num
import numpy as np

def main():
    # Sample Input: Edge Lists
    edgeList = [(1,2),(2,1),(3,2),(2,3),(4,5)]
    edgeList2 =[(1,2),(1,3),(2,3),(4,5),(6,7),(7,8)]
    numVertices = 8
    directed = False
    
    # Output - Returns a list of sets, with each set representing the vertices in a connected
    # component.
    print(connected(edgeList2, numVertices, directed))


    

def connected(edgeList, numVertices,directed):
    # Generate adjacency matrix for input grapg from edgeList
    adjMat = adjMatrixGenerator(edgeList, numVertices, directed)
    
    return components(adjMat, numVertices)



# Returns a list of sets. Each set in the list is a connected component.
def components(adjMat, numVertices):
    componentList = []
    connectedAdj = np.zeros([numVertices, numVertices], dtype = int)
    for i in range(1,numVertices + 1):
        connectedAdj = connectedAdj + paths(adjMat, i)
    for row, vertex1 in enumerate(connectedAdj): 
        for col  in range(row+1,len(vertex1)):
            added = False
            if connectedAdj[row][col] >= 1 and connectedAdj[col][row] >= 1:
                if len(componentList) == 0:
                    componentList.append({row + 1,col + 1}) 
                else:
                    for index, myset in enumerate(componentList):
                        if (row+1 in myset) or (col+1 in myset):
                            componentList[index] = componentList[index] | {row + 1,col + 1}
                            added = True
                            break
                    if not(added):
                        componentList.append({row + 1,col + 1})
    loneComponents = []
    if len(componentList) < numVertices:      
        for vertex in range(numVertices):
            if not(any(((vertex + 1) in element) for element in componentList)):
                loneComponents.append({vertex+1})
    componentList.extend(loneComponents)
    return componentList



# Returns showing how many paths of length n exist for a graph represented by adjMatrix
def paths(adjMatrix, n):
    adjMatNP = np.array(adjMatrix)
    pathsMatNP = adjMatNP
    for i in range(n-1):
        pathsMatNP =  np.dot(pathsMatNP,adjMatNP)
    # pathsMathNP = adjMatrix ^ n
    return pathsMatNP


def adjMatrixGenerator(edges, numVertices, directed = False):
    adjMatrix = np.zeros([numVertices, numVertices], dtype = int)
    
    for pair in edges:
        adjMatrix[pair[0]-1][pair[1]-1] += 1
        if not directed:
            adjMatrix[pair[1]-1][pair[0]-1] += 1

    return adjMatrix
    

if __name__ == "__main__":
    main()