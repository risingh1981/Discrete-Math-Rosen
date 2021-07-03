# Chapter 10, Computer Project 7: Given the vertex pairs associated to the edges of 
# an undirected graph and the number of times each edge appears, construct an 
# incidence matrix for the graph.

def main():
    # Input: Dict with keys as vertex pairs and values as number of times the 
    #        edge appears. 
    edges = {(1,4):1,(1,5):1,(2,3):1,(2,4):1,(2,5):1,(3,5):1}
    edges2 = {(1,4):2,(1,5):1,(2,3):1,(2,4):1,(2,5):1,(3,5):1}
    # Output: Function returns incidence matrix and the indexing used for the edges.
    print(incidenceMatrixGenerator(edges))
    print(incidenceMatrixGenerator(edges2))


def incidenceMatrixGenerator(edges):
    maxVertex = max(ele for pair in edges for ele in pair)
    numEdges = len(edges)
    incidenceMatrix = [([0] * numEdges) for _ in range(maxVertex)]
    edgeNumbering = {}
    for edgeNumber, edge in enumerate(edges):
        for times in range(edges[edge]):
            incidenceMatrix[edge[0]-1][edgeNumber] += 1
            incidenceMatrix[edge[1]-1][edgeNumber] += 1
        edgeNumbering[edgeNumber + 1] = edge
    return incidenceMatrix, edgeNumbering


if __name__ == "__main__":
    main()

