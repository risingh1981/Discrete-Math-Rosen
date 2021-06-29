# Chapter 9, Computer Project 5: Given a positive integer n, determine the number 
# of transitive relations on a set with n elements.
# Math Foundation: There is no known formula to determine the number of transitive 
# relations(Tₙ) on a set with n elements. The sequence OEIS A006905: [1, 2, 13, 171, 
# 3994, 154303, 9415189, 878222530, 122207703623, 24890747921947, 7307450299510288, 
# 053521546333103057, 1797003559223770324237, 1476062693867019126073312, 
# 1679239558149570229156802997, 2628225174143857306623695576671, 
# 5626175867513779058707006016592954, 16388270713364863943791979866838296851, 
# 64662720846908542794678859718227127212465] defines Tₙ. As can be seen the number grows 
# very quickly.
# https://en.wikipedia.org/wiki/Transitive_relation#Counting_transitive_relations

from numpy import matrix
from itertools import product, combinations
from time import perf_counter_ns

def main():
    # Input Set A
    setA =[1,2,3,4]
    # Output Results
    start = perf_counter_ns()
    transRels = generateAllTransitive(setA)
    end = perf_counter_ns()
    totTime = end - start
    print(f"Number of Transitive relations on set {setA}: {len(transRels)}.")
    print(f"Total Time: {totTime / (10 ** 9)} s")
    

def generateAllTransitive(inputSet):
    return filterTransitive(generateAllRelations(inputSet))

def filterTransitive(allRelations):
    allTrans = [relation for relation in allRelations if transitive(relation)]
    return allTrans

def transitive(relation):
    squared = matrix(relation) ** 2
    dim = len(relation)
    for i in range(dim):
        for j in range(dim):
            if (squared[i,j] >= 1) and (relation[i][j] == 0):
                return False
    return True

def generateAllRelations(inputSet):
    # Cartesian product AxA, where A is the inputSet. if n = len(A), n^2 is len(aXa)
    aXa = list(product(inputSet, repeat = 2))
    n = len(inputSet)
    # Generate r-combinations of the Cartesian product of values of r=0 through r=len(aXa)
    # There are 2^(n^2) arrays representing relations in allRelArr
    allRelArr = [[[0 for x in range(0,n)] for y in range(0,n)] for z in range(0, 2 ** (n ** 2))]
    index = 0
    for i in range(0, len(aXa) + 1):
        combos = combinations(aXa,i)
        for combo in combos:
            for item in combo:
                allRelArr[index][item[0]-1][item[1]-1] = 1
            index += 1
    return allRelArr



if __name__ =="__main__":
    main()