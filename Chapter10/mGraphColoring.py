# Algorithm to determine if a graph can be colored with m colors using 
# backtracking.
# Algorithm:
# 1)Create a recursive function that takes the graph, current index, number of 
#   vertices, and output color array.
# 2)If the current index is equal to the number of vertices. Print the color 
#   configuration in output array.
# 3)Assign a color to a vertex (1 to m).
# 4)For every assigned color, check if the configuration is safe, (i.e. check if 
#   the adjacent vertices do not have the same color) recursively call the function 
#   with next index and number of vertices
# 5)If any recursive function returns true break the loop and return true.
# 6)If no recursive function returns true then return false.


def main():
    # Input Adjacency Matrix of Graph
    # Ex of 3-colorable graph
    graphMatrix = [[ 0, 1, 1, 1 ],[ 1, 0, 1, 0 ],[ 1, 1, 0, 1 ],[ 1, 0, 1, 0 ]]
    m = 3
    # Output
    print(f"Graph {m}-colorable: {graphColoring(graphMatrix, m)}")

# m colors (1,2,...,m)
# k = current node
# colorArr = holds color (1-m) for each vertex. Vertex 1 at index 0 of colorArr
def graphColoring(adjMatrix, m):
    numVertices = len(adjMatrix)
    colorArr = [0 for _ in range(0,numVertices)] 
    currentNode = 0
    # Recursive helper function
    boolColorable = graphColoringHelper(adjMatrix, numVertices, currentNode, m, colorArr)
    return boolColorable if boolColorable else False

def graphColoringHelper(adjMatrix, numVertices, currentNode, m, colorArr):
    #Loop through colors:1 to m
    for c in range(1,m+1):
        if isSafe(c, currentNode, adjMatrix, numVertices, colorArr):
            colorArr[currentNode] = c
            if (currentNode + 1 < numVertices):
                return graphColoringHelper(adjMatrix, numVertices, currentNode + 1, m, colorArr)
            else:
                return colorArr
                

def isSafe(c, currentNode, adjMatrix, numVertices, colorArr):
    for i in range(0, numVertices):
        if (adjMatrix[currentNode][i] == 1) and (c == colorArr[i]):
            return False
    return True


    

    

if __name__ == "__main__":
    main()