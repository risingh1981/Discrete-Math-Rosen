# Chapter 10, Computer Project 7: Given an *incidence matrix* of an undirected graph, 
# list its edges and give the number of times each edge appears.

def main():
    # Input
    incMatrix = [[2, 1, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0], [0, 0, 1, 0, 0, 1], [2, 0, 0, 1, 0, 0], [0, 1, 0, 0, 1, 1]]
    # Edges {1: (1, 4), 2: (1, 5), 3: (2, 3), 4: (2, 4), 5: (2, 5), 6: (3, 5)}) Edge 1 appears twice.

    # Output
    print(edgeGenerator(incMatrix))
    # {(1, 4): 2, (1, 5): 1, (2, 3): 1, (2, 4): 1, (2, 5): 1, (3, 5): 1}

def edgeGenerator(incMatrix):
    numVertices = len(incMatrix)
    edgesDict = {}
    for col in range(len(incMatrix[0])):
        edge = []
        count = 0
        for row in range(numVertices):
            if incMatrix[row][col] >= 1:
                count = incMatrix[row][col]
                edge.append(row+1)
        edgesDict[tuple(edge)] = count
    return edgesDict



if __name__ == "__main__":
    main()