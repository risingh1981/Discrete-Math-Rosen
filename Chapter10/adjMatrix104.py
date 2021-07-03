# Chapter 10, Computer Project 4: Given the vertex pairs associated to the edges of 
# a graph, construct an adjacency matrix for the graph. (Produce a version that
# works when loops, multiple edges, or directed edges are present.)


def main():
    # Input - Enter array of tuples for edges in graps. If two vertices have multiple
    # edges, enter as many tuples of that vertex pair as there are edges.
    graph1 = [(1,3),(1,3),(1,5),(1,6),(1,7),(2,3),(2,5),(2,6),(3,4),(4,5),(4,6),(4,7)]
    graph2 = [(1,2),(1,5),(1,6),(2,3),(2,4),(2,5),(2,6),(3,4),(3,6),(4,5),(4,6),(5,6)]
    # Output
    print(adjMatrixGenerator(graph1, True))
    print(adjMatrixGenerator(graph2))


# Function will generate adjacency matrix from input an array of tuples representing
# edges and optional parameter directed, which can be set to True if the edges are directed.
def adjMatrixGenerator(edges, directed = False):
    maximum = max(ele for pair in edges for ele in pair)
    adjMatrix = [([0] * maximum) for _ in range(maximum)]
    
    for pair in edges:
        adjMatrix[pair[0]-1][pair[1]-1] += 1
        if not directed:
            adjMatrix[pair[1]-1][pair[0]-1] += 1

    return adjMatrix
    


if __name__ == "__main__":
    main()