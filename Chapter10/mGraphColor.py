import numpy as np
from DiscreteMathRosen.Chapter10.matrixReader import dictGraphs
from copy import copy

def main():
    trialDict = dictGraphs(80)
    

   
   
def graphColor(G, m,x = [], found = [],k = 0):
    n = len(G)
    if (k == 0):
        x = ["" for _ in range(len(G))]
        found = []
    for c in range(1,m+1):
        if found:
            break
        if (isSafe(k,c,G,x)):
            x[k] = c
            if ((k+1) < n):
                graphColor(G, m, x, found, k+1)
            else:
                found.extend(x)
                return
    return found 

def isSafe(k,c,G,x):
    n = len(G)
    for i in range(k):
        if (G[k][i] == 1) and (c == x[i]):
            return False
    return True

if __name__ == "__main__":
    main()