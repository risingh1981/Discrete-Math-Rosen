# Chapter 10, Computer Project 13: Given the vertex pairs associated to the edges of a 
# multigraph, determine whether it has an Euler circuit and, if not, whether it has an Euler path. 
# Construct an Euler path or circuit if it exists.
# Math Foundation: 
# Definitions: Euler circuit transverses every edge once and ends up at starting vertex.
# Euler Path transverses every edge once and ends up at a vertex different than starting vertex.
# Theorem: A connected multigraph with at least two vertices has an Euler circuit if and 
# only if each of its vertices has even degree.
# Theorem: A connected multigraph has an Euler path but not an Euler circuit if and only 
# if it has exactly two vertices of odd degree.
# One way to is to create a function to find a Eulerian Circuit and if you want a Eulerian
# Path instead, just add an edge to connect the start and end points(2 odd vertices) of the 
# Eulerian Path, find the circuit and remove the added edge

# Recursive Algorithm(Program Based on this algorithm, not Fleury's):
# procedure FindEulerPath(V)
# 1. iterate through all the edges outgoing from vertex V;
#      remove this edge from the graph,
#      and call FindEulerPath from the second end of this edge;
# 2. add vertex V to the answer.
#
# Fleury's Algorithm:
# If looking for circuit, start at any vertex. If path start at an odd degree vertex.
# While edge list is not empty:
# 1) Pick an edge starting with current vertex as long as its not a bridge, unless only bridges are left.
# 2) Remove this edge from edgeList. Set current vertex to end point of this edge.


def main():
    # Input: Enter edgeList of undirected graph/multigraph
    # EP (2,4)
    g1 = [(1,4),(2,4),(2,3),(3,4),(1,2)]
    # EP (2,4)
    g2 = [(1,7),(3,7),(3,6),(3,4),(4,5),(4,6),(5,6),(6,7),(1,2),(2,3),(2,7)]
    # Neither
    g3 = [(1,2),(1,6),(1,7),(2,3),(2,7),(3,4),(3,7),(4,5),(4,7),(5,6),(5,7),(6,7)]
    # EC    
    g4 = [(1,2),(1,5),(2,3),(2,4),(2,5),(3,4),(4,6),(4,7),(5,6),(5,9),(6,9),(6,7),(7,8),(7,11), (8,9),(8,10),(8,11),(9,10)]
  
    # Output
    print(euler(g1))
    print(euler(g2))  
    print(euler(g3))
    print(euler(g4))


def euler(edgeList):
    # Degree function takes list of edges as input and returns as output a dictionary with each 
    # vertex as key and a tuple (i,o) as value with i = in-degree and o = out-degree
    vertDegrees = degree(edgeList)
    result = isEulerian(vertDegrees)
    # Determines which function to call based on whether a Euler Path or a circuit exists.
    if result:
        if result == "Euler Circuit":
            return "Euler Circuit", eulerCircuit(edgeList)
        else:
            return "Euler Path", eulerPath(edgeList, result)
    else:
        return "None", False

def eulerCircuit(edgeList):
    startingVertex = edgeList[0][0]
    # Call recursive helper function eulerCircuitRec
    circuit = []
    eulerCircuitRec(edgeList, startingVertex, circuit)
    return circuit
    

def eulerCircuitRec(edgeList, startingVertex, circuit):
    for edge in edgeList:
        if edge[0] == startingVertex:
            edgeList.remove(edge)
            eulerCircuitRec(edgeList, edge[1], circuit)
        elif edge[1] == startingVertex:
            edgeList.remove(edge)
            eulerCircuitRec(edgeList,edge[0], circuit)
    circuit.append(startingVertex)

    
def eulerPath(edgeList, result):
    edgeList.append((result[0],result[1]))
    circuit = []
    eulerCircuitRec(edgeList, result[0], circuit)
    eulerPath = circuit[1:]
    return eulerPath

# Function returns string "Euler Circuit" if such a circuit exists, a list of starting/ending 
# vertex if Euler Path exists, or False if neither exist.
def isEulerian(vertDegrees):
    even = 0
    oddVerts = []
    for vertex in vertDegrees:
        if (vertDegrees[vertex] % 2 == 0):
            even += 1
        else:
            oddVerts.append(vertex)

    if even == len(vertDegrees):
        return "Euler Circuit"
    elif len(oddVerts) == 2:
        return oddVerts
    else:
        return False

# Returns a dictionary with keys as vertices and values as degree of such vertex.
def degree(edgeList):
    degreeDict = {}
    for edge in edgeList:
        for vertex in edge:
            if vertex in degreeDict:
                degreeDict[vertex] += 1
            else:
                degreeDict[vertex] = 1
    return degreeDict




if __name__ == "__main__":
    main()