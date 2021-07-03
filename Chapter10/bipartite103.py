# Chapter 10, Computer Project 3: Given the list of edges of a simple graph, 
# determine whether the graph is bipartite.
# Math Note: A simple graph is bipartite if and only if it is possible to 
# assign one of two different colors to each vertex of the graph so that no 
# two adjacent vertices are assigned the same color.
from DiscreteMathRosen.Chapter10.mGraphColoring import graphColoring
def main():
    # Input
    # Ex of bipartitie
    adjMatrix1 = [[0,0,1,0,1,1,1],[0,0,1,0,1,1,0],[1,1,0,1,0,0,0],[0,0,1,0,1,1,1],[1,1,0,1,0,0,0],[1,1,0,1,0,0,0],[1,0,0,1,0,0,0]]
    # Ex of non-bipartite
    adjMatrix2 =[[0,1,0,0,1,1],[1,0,1,1,1,1],[0,1,0,1,0,1],[0,1,1,0,1,1],[1,1,0,1,0,1],[1,1,1,1,1,0]]

    # Output
    print(f"Bipartite: {bipartite(adjMatrix1)}")
    print(f"Bipartite: {bipartite(adjMatrix2)}")
    '''
    Bipartite: True
    Bipartite: False
    '''
    


def bipartite(adjMatrix):
    return True if graphColoring(adjMatrix,2) else False

if __name__ == "__main__":
    main()