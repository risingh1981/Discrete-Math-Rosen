# Chapter 10, Computer Project 1: Given the vertex pairs associated to the edges 
# of an undirected graph, find the degree of each vertex. Note, an undirected graph
# with loops and multiple edges is called a psuedograph/mixed undirected graph. 
# Simple undirected graph doesn't have loops or multiple edges.

def main():

    # Input - Enter vertex pairs for undirected edges.
    graph = [(1,1),(1,2),(2,3),(2,4),(3,1),(3,3),(4,3),(4,1)]

    # Output - degree of each vertex
    print(degree(graph))

def degree(graph):
    degreeOfV = {}
    for pair in graph:
        for vertex in pair:
            if vertex in degreeOfV:
                degreeOfV[vertex] += 1
            else:
                degreeOfV[vertex] = 1
    return degreeOfV 



if __name__ == "__main__":
    main()

    