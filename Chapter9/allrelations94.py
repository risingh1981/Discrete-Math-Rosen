# Chapter 9, Computer Project 4: Given a positive integer n, display all the 
# relations on a set with n elements.
# Math Foundation: A relation on a Set A is a subset of the cartesian product, A x A.
# So all relations on set A would be the power set of the cartesian product A x A.
# The cartesian product A x A has n^2 elements.
# Each subset of A x A defines a relation. All such subsets are the powerset of AxA.
# The powerset of a set with n elements contains 2^n elements.
# So a set A with n elements would have 2^(n^2) possible relations defined on it.

from DiscreteMathRosen.Chapter6.rpermswithrep69 import rpermswithrep
from DiscreteMathRosen.Chapter6.combs68 import allcombinations
from itertools import product, combinations

def main():
    # Input
    n = 3

    # List representing set A with n elements:
    arrA = [x for x in range(1,n + 1)]
    # Output
    print(allrelations(arrA))

# Using self-created allcombinations function and r-pers but pythons provided functions are
# faster   
def allrelations2(arrA):
    aXa2 = rpermswithrep(arrA, 2)
    allRelSet2 = [[]]
    allRelSet2.extend(allcombinations(aXa))
    return allRelSet2

def allrelations(arrA):
    # Cartesian product of AxA
    aXa1 = list(product(arrA, repeat = 2))
    # Generate r-combinatinos of the Cartesian product of values of r=0 through r=len(aXa)
    allRelSet = []
    for i in range(0,len(aXa1)+1):
        allRelSet.extend(list(combinations(aXa1,i)))
    


    

if __name__ == "__main__":
    main()