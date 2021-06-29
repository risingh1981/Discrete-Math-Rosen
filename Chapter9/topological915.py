# Chapter 9, Computer Project 15: Given a partial ordering on a finite set, find a 
# total ordering compatible with it using topological sorting.
# Math Foundation: A relation R on a set S is called a partial ordering or partial 
# order if it is reflexive, antisymmetric, and transitive.
# The elements a and b of a poset (S, ) are called comparable if either a < b or 
# b < a. When a and b are elements of S such that neither a < b nor b < a, 
# a and b are called incomparable.
# If (S, <) is a poset and every two elements of S are comparable, S is considered a 
# totally ordered or linearly ordered set.
# A total ordering <= is said to be compatible with the partial ordering R if 
# a <= b whenever aRb. Constructing a compatible total ordering from a partial
# ordering is called topological sorting.
# Impt Lemma for Toplogical Sorting:
#   Every finite nonempty poset (S, <) has at least one minimal element.
# Algorithm for Topological Sorting mentioned in Rosen.
# procedure topological sort ((S, <): finite poset)
# k := 1
# while S != ∅
#   ak : = a minimal element of S {such an element exists by Lemma mentioned above}
#   S : = S − {ak}
#   k : = k + 1
# return a1, a2, . . . , an {a1, a2, . . . , an is a compatible total ordering of S}
# 
# Topological sorting has an application to the scheduling of projects.
# Algorithms from Online Research:
# Kahn's Algorithm:
# 4 main tasks:
# 1) Count and store the in-degree of all nodes in the graph.
# 2) Identify nodes with 0 in-degree. (Same as finding minimal element)
#    Add each node to a set that will be iterated over and append each node to a 
#    list that will contain the sorted nodes. 
# 3) While the set containing nodes with an in-degree of 0 is not empty, remove a 
#    node. For each node removed, iterate over its edges, decrementing the stored 
#    in-degree of each destination node in the edge. If a node now has an in-degree 
#    of 0, add it to the set and list per step 2.
# 4) Finally, return the list to which each node was appended. This is a topological
#    sort.


class Node:
    def __init__(self,val, relatedTo = None):
        self.val = val
        self.indegree = 0
        if relatedTo == None: 
            self.relatedTo = []
        else:
            self.relatedTo = [relatedTo]
    
    def decrement(self):
        self.indegree -= 1
    
    def increment(self):
        self.indegree += 1
    
    def relateTo(self, element):
        self.relatedTo.append(element)

def main():
    # Input
    # The partial ordering {(a, b) |a divides b} on {1, 2, 3, 4, 6, 8, 12}.
    #inputPO1 = [(1,1),(1,2),(1,3),(1,4),(1,6),(1,8),(1,12),(2,2),(2,4),(2,6),(2,8),(2,12),(3,3),(3,6),(3,12),(4,4),(4,8),(4,12),(6,6),(6,12),(8,8),(12,12)]
    #inputPO = [(5, 2),(5, 0),(4, 0),(4, 1),(2, 3),(3, 1)]
    inputPO = [("Z", "R"),("R", "Y"),("R", "P"),("Y", "O"),("P", "O"),("Y", "Q"),("Q","T")]
    
    # Output
    print(f"Topological Sort: {topologicalSort(inputPO)}.")
    



def topologicalSort(inputPO):
    sorted = []
    degreeDict = processInput(inputPO)
    while bool(degreeDict):
        minimal = removeMinimal(degreeDict)
        sorted.append(minimal)
    return sorted

def removeMinimal(degreeDict):
    for key in degreeDict:
        if (degreeDict[key].indegree == 0):
            toDecrement = degreeDict[key].relatedTo
            keyToRemove = key
            break
    if toDecrement:
        for value in toDecrement:
            keyToDecrement = keyOfnodeWithVal(degreeDict, value)
            degreeDict[keyToDecrement].decrement()
    minimal = degreeDict[keyToRemove].val
    del degreeDict[keyToRemove]
    return minimal
    

def keyOfnodeWithVal(degreeDict,value):
    for key in degreeDict:
        if (degreeDict[key].val == value):
            return key
    return None

def processInput(inputPO):
    degreeDict = {}
    for pair in inputPO:
        if (pair[0] not in degreeDict) and (pair[0] != pair[1]):
            degreeDict[pair[0]] = Node(pair[0],pair[1])
        elif (pair[0] not in degreeDict):
            degreeDict[pair[0]] = Node(pair[0])
        elif (pair[0] != pair[1]):
            degreeDict[pair[0]].relateTo(pair[1])
        if (pair[0] != pair[1]) and pair[1] not in degreeDict:
             degreeDict[pair[1]] = Node(pair[1])
             degreeDict[pair[1]].increment()
        elif (pair[0] != pair[1]) and pair[1] in degreeDict:
            degreeDict[pair[1]].increment()

    return degreeDict

   

if __name__ == "__main__":
    main()