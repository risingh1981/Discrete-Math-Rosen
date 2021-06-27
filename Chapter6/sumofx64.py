# Chapter 6, Program 4: Given an equation x1 + x2 +· · ·+xn = C, where C is a
# constant, and x1, x2, . . . , xn are nonnegative integers, list
# all the solutions.

# Not working. Do after studying integer partitions.


from itertools import combinations_with_replacement
def main():
    # Input: Enter value for constant c.
    c = 5
    #generate(c)
    pairsArr = pairs(5)
    #delete([(4, 0), (3, 1), (2, 2), (1, 3)])
    generate(pairsArr)



def generate(pairsArr):
    partitions = []
    for pairsB in pairsArr[len(pairsArr) - 1]:
        partitions.append(pairsB)
    print(partitions)

    for level in range(len(pairsArr) - 1, -1, -1):
        input(f"level:{level}")
        for onepair in range(0, len(pairsArr[level])):
            for ele in range(0,len(pairsArr[level][onepair])):
                # the element is pairsArr[level][onepair][ele]
                input(f"pairsArr[level][onepair][ele]: {pairsArr[level][onepair][ele]}")
                input(f"len(pairsArr): {len(pairsArr)}")
                if (pairsArr[level][onepair][ele] == len(pairsArr)) or (pairsArr[level][onepair][ele] == 0) or (pairsArr[level][onepair][ele] == 1):
                    continue
                for i in range(0,len(pairsArr[pairsArr[level][onepair][ele]-1])):
                    newpair = pairsArr[level][onepair].copy()
                    input(f"after copy: newpair = {newpair}")
                    tocopy = newpair.copy()
                    #partitions.append(tocopy)
                    print(f"partitions after append: {partitions}")
                    newpair.remove(pairsArr[level][onepair][ele])
                    input(f"newpair after remove: {newpair}") #newpair[0] = remaining element
                    newpair = newpair + pairsArr[len(pairsArr) - newpair[0]-1][i]
                    input(f"newpair = {newpair}")
                    partitions.append(newpair)
                    input(f"paritions: {partitions}")

                    




    
    # New Pairs: [[[1, 0]], [[2, 0], [1, 1]], [[3, 0], [2, 1]], [[4, 0], [3, 1], [2, 2]], [[5, 0], [4, 1], [3, 2]]]

def pairs(n):
    pairsArr = [[] for i in range(n)]
    #pairsArr[0].append([1])
    
    for j in range(0,n):
        for i in range(0,j+1):
            print(f"j:{j} i:{i}")
            pairsArr[j].append((j-i+1,i))
    print(f"Pairs: {pairsArr}")
    
    for i in range(0,len(pairsArr)):
        newPair = delete(pairsArr[i])
        pairsArr[i] = newPair
    
    print(f"New Pairs: {pairsArr}")
    # New Pairs: [[[1, 0]], [[2, 0], [1, 1]], [[3, 0], [2, 1]], [[4, 0], [3, 1], [2, 2]], [[5, 0], [4, 1], [3, 2]]]
    return pairsArr


    '''    
    for unit in pairsArr:
        newunit = delete(unit)
        for tupleA in unit
    '''
            
    #print(pairsArr)
    

def delete(arr):
    toDelete = []
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if set(arr[i]) == set(arr[j]):
                toDelete.append(i)
    newArr = []
    for idx in range(0,len(arr)):
        if idx not in toDelete:
            newArr.append(sorted(arr[idx], reverse=True))
    newArr = sorted(newArr, reverse=True)
    #print(newArr)
    return newArr





if __name__ == "__main__":
    main()