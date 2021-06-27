# Chapter 6, Computer Project 5: Given a positive integer n, list all the permutations of the
# set {1, 2, 3, . . . , n} in lexicographic order.
# Algorithm to generate permutations in lexicographic order from book Discrete Math and its Apps by Rosen:
# Start with [a1,a2,...,an]
# Repeat till result permutation is [an,...,a2,a1]
# 1) Find largest j such that a(j) > a(j-1).
# 2) Swap a(j) and a(j-1). put a(j) through a(n) in increasing order.
from itertools import permutations
from time import perf_counter_ns


def main(): 
    # Input for program is n, for the program to generate all permutations of the set {1,2,...,n}
    # Input generated in timing section
    
    # Output
    for n in range(2,11):
        start = perf_counter_ns()
        myperms = allpermutations(n)
        end = perf_counter_ns()
        mytime = end - start

        start = perf_counter_ns()
        pyinitperm = [x for x in range(1,n+1)]
        pyperms = list(permutations(pyinitperm))
        end = perf_counter_ns()
        pytime = end - start
        print(f"Number of perms for n = {n}: {len(myperms)}.")
        if (n <= 5):
            print(f"For n = {n}: pytime: {pytime} ns  mytime = {mytime} ns")
        else:
            print(f"For n = {n}: pytime: {pytime/(10**9)} s  mytime = {mytime/(10**9)} s")
# Output Timing Summary:
'''
Timing:
Number of perms for n = 2: 2.
For n = 2: pytime: 2700 ns  mytime = 14900 ns
Number of perms for n = 3: 6.
For n = 3: pytime: 4800 ns  mytime = 33400 ns
Number of perms for n = 4: 24.
For n = 4: pytime: 8500 ns  mytime = 95100 ns
Number of perms for n = 5: 120.
For n = 5: pytime: 41800 ns  mytime = 497300 ns
Number of perms for n = 6: 720.
For n = 6: pytime: 0.0010922 s  mytime = 0.0021091 s
Number of perms for n = 7: 5040.
For n = 7: pytime: 0.0010145 s  mytime = 0.0146672 s
Number of perms for n = 8: 40320.
For n = 8: pytime: 0.0110169 s  mytime = 0.0862946 s
Number of perms for n = 9: 362880.
For n = 9: pytime: 0.0814001 s  mytime = 0.722798 s
Number of perms for n = 10: 3628800.
For n = 10: pytime: 0.5719638 s  mytime = 8.6336182 s
''' 
    
    
# Generates all permutations with help of function nextpermutation by looping until the nextpermutation
# generated is the final permutation.
def allpermutations(n, identityperm = False):
    if (identityperm == False):
        identityperm = [x for x in range(1,n+1)]
    finalperm = list(reversed(identityperm))
    a = []
    a.append(identityperm.copy())
    while (identityperm != finalperm):
        identityperm = nextpermutation(identityperm)
        nextentry = identityperm.copy()
        a.append(nextentry)
    return a


# Function nextpermutation returns next permutation in lexicographic order or returns false if input 
# permutation is last permutation in lexicographic order, namely [n,n-1,...,2,1]
# Algo: 1)Find first int from right that is greater than the int to its left, call index of int on left: 
# step1index.
# 2) from int in position j+1 to n-1, find smallest int greater than the int at index j. Swap them.
# 3) Put int in positions j+1 to n-1 in increasing order
def nextpermutation(perm):
    step1index = -1
    permlen = len(perm) # Save len of perm as it will need to be accessed several times.
    # Step 1: Determine step1index, index of first int from right that is greater than the int to its right.
    for i in range(permlen-1, 0, -1):
        if perm[i] > perm[i-1]:
            step1index = i - 1
            break
    # Step 2a: Find index of smallest int greater than int at index step1index.
    mindiff = max(perm) # Set min diff to max possible, so choose len(perm) as its value, will be updated.
    for j in range(step1index + 1, permlen):
        if perm[step1index] < perm[j]:
            if (mindiff > (perm[j] - perm[step1index])):
                mindiff = perm[j] - perm[step1index]
                step2index = j
    # Step 2b: Swap ints at index step1index and step2index
    perm[step1index],perm[step2index] = perm[step2index], perm[step1index]

    # Step 3: Put in increasing order the ints in indices (step1index+1) to (permlen - 1)
    if ((step1index != -1) and step1index != (permlen - 1)):
        newperm = sorted(perm[step1index+1:])
        newperm = perm[:step1index+1] + newperm
        return newperm # newperm at this point is next perm after input perm in lexicographic order.
    return False if ((step1index == -1)) else perm #False if the input perm was largest perm in lexicographic
                                                   #order, else return perm since step 3 was skipped.


if __name__ == "__main__":
    main()

