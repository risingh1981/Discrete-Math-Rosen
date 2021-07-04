# Chapter 10, Computer Project 2: Given the ordered pairs of vertices associated 
# to the edges of a directed graph, determine the in-degree and outdegree of 
# each vertex.
# Simple directed graph - No loops. No multiple Edges.
# Directed Multigraph/Mixed - Has loops and multiple edges

def main():

    # Input - Enter vertex pairs for directed edges.
    graph = [(1,1),(1,2),(1,3),(2,1),(2,3),(2,4),(3,1),(3,3),(3,4),(4,3),(4,1)]

    # Output - Dict w/ key = vertex and tuple=(inDegree, outDegree) of each vertex.
    print(degree(graph))
# Returns a dictionary of tuples, where the key is the vertex and its associated tuple
# is (i,o), where i is in degree and o is out degree.
def degree(graph):
    degreeOfV = {}
        
    for pair in graph:
        for num, vertex in enumerate(pair):
                if (num == 0) and (vertex in degreeOfV):
                    degreeOfV[vertex] = (degreeOfV[vertex][0],degreeOfV[vertex][1] + 1)
                elif (num == 1) and (vertex in degreeOfV):
                    degreeOfV[vertex] = (degreeOfV[vertex][0] + 1,degreeOfV[vertex][1])
                elif (num == 0) and (vertex not in degreeOfV):
                    degreeOfV[vertex] = (0,1)
                else:
                    degreeOfV[vertex] = (1,0)
    return degreeOfV 


if __name__ == "__main__":
    main()