# Chapter 10, Computer Project 5: Given an adjacency matrix of a graph, list the 
# edges of this graph and give the number of times each edge appears.


def main():
    # Input - adjacency matrix of graph
    # Directed graph with multiple edges(matrix does not need to be symmetric)
    graph1 = [[0, 0, 2, 0, 1, 1, 1], [0, 0, 1, 0, 1, 1, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
    # Undirected graph with multiple edges
    graph1u = [[0, 0, 2, 0, 1, 1, 1], [0, 0, 1, 0, 1, 1, 0], [2, 1, 0, 1, 0, 0, 0], [0, 0, 1, 0, 1, 1, 1], [1, 1, 0, 1, 0, 0, 0], [1, 1, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 0, 0]]
    # Undirected graph w/out multiple edges
    graph2 = [[0, 1, 0, 0, 1, 1], [1, 0, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1], [0, 1, 1, 0, 1, 1], [1, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 0]]

    # Output
    
    print(edgeGenerator(graph1, False)) # Since graph1's matrix is of an undirected 
                                        # graph, pass value False also, or it will raise
                                        # ValueError for matrix not being symmetric.
    print(edgeGenerator(graph1u))
    print(edgeGenerator(graph2))
    
    


# Setting undirected to False means input matrix represents a directed graph.
def edgeGenerator(adjMatrix, undirected = True):
    dim = len(adjMatrix)
    edges = []
    if not undirected:
        for row in range(dim):
            for col in range(dim):
                if adjMatrix[row][col] >= 1:
                    edges.extend((row+1,col+1) for _ in range(adjMatrix[row][col]))       
    else:
        if not checkSymmetric(adjMatrix):
            raise ValueError("Input adjacency matrix does not represent an undirected graph as its not symmetric.")
        for row in range(dim):
            for col in range(row, dim):
                if adjMatrix[row][col] >= 1:
                    edges.extend((row+1,col+1) for _ in range(adjMatrix[row][col]))

    return edges

def checkSymmetric(adjMatrix):
    dim = len(adjMatrix)
    for r in range(dim):
        for c in range(dim):
            if adjMatrix[r][c] != adjMatrix[c][r]:
                return False
    return True

if __name__ == "__main__":
    main()