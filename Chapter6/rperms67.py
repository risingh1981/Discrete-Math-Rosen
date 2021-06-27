# Chapter 6, Computer Project 7: Given a positive integer n and a nonnegative integer r
# not exceeding n, list all the r-permutations of the set {1, 2, 3, . . . , n} in lexicographic order.
# The algorithm given in Introductory Combinatorics by Brualdi involves generating r-subsets of input set
# and for each r-subset permuting it and then determining the lexicographic ordering using the formula 
# which will be discussed in the comments preceding the function in the program that uses the formula.
from rcombs66 import rcombs
from permslexi65 import allpermutations
from permscombs61 import permutations, combinations
from itertools import permutations

def main():
    # Input:
    r = 3
    n = 5
    
    # Output
    answer = rperms(r,n)
    # Compare size of answer with pythons list of r-permutations
    print(len(answer) == (len(list(permutations([x for x in range(1,n+1)], r))))) # True
    
    
# Generate all r-permutations of a set {1,2,...,n} inlexicographic order.   
def rperms(r,n):
    # Generate r-combinations:
    rcombsArr = rcombs(r,n)
    # Generate all permutations of the r-combinations
    allpermsArr = []
    for rcomb in rcombsArr:
        allperms = allpermutations(r, rcomb)
        allpermsArr = allpermsArr + allperms
    allpermsArr = lexicographicorder(allpermsArr)
    return allpermsArr
    

# Sort the list of permutations
def lexicographicorder(listOfPerms):
    listOfPerms = sorted(listOfPerms)
    return listOfPerms



if __name__ == "__main__":
    main()