# This is an extension to problem 5 from Chapter 6 of Discrete Math and Its Apps by Rosen using the 
# algorithm for generating permutations given in Introductory Combinatorics by Brualdi.
# Rosen's algorithm is about twice as fast but it could have to do with implementation; though, neither 
# are optimal.
from itertools import permutations
from permslexi65 import allpermutations
from time import perf_counter_ns

def main():
    # Input - value for n: number of elements in initital permutation of numbers 1 through n
    # Generate array

    for n in range(2,11):
        start = perf_counter_ns()
        myperms1 = allpermutations(n)
        end = perf_counter_ns()
        mytime1 = end - start

        start = perf_counter_ns()
        myperms2 = generator(n)
        end = perf_counter_ns()
        mytime2 = end - start

        start = perf_counter_ns()
        pyinitperm = [x for x in range(1,n+1)]
        pyperms = list(permutations(pyinitperm))
        end = perf_counter_ns()
        pytime = end - start
        print(f"Number of perms for n = {n}: {len(myperms1)}.")
        if (n <= 5):
            print(f"For n = {n}: pytime: {pytime} ns, mytime1: {mytime1} ns, mytime2: {mytime2}")
        else:
            print(f"For n = {n}: pytime: {pytime/(10**9)} s,  mytime1 = {mytime1/(10**9)} s, mytime2: {mytime2/(10**9)}")
        
# Output for Timing Comparison between pythons permutations function and Algorithms from Rosen and Brualdi.
'''
Number of perms for n = 2: 2.
For n = 2: pytime: 5200 ns,  mytime1: 31100 ns, mytime2: 38900 ns
Number of perms for n = 3: 6.
For n = 3: pytime: 7000 ns, mytime1: 42900 ns, mytime2: 411200 ns
Number of perms for n = 4: 24.
For n = 4: pytime: 73800 ns, mytime1: 88500 ns, mytime2: 156300 ns
Number of perms for n = 5: 120.
For n = 5: pytime: 13900 ns, mytime1: 341600 ns, mytime2: 387600 ns
Number of perms for n = 6: 720.
For n = 6: pytime: 0.0001212 s,  mytime1 = 0.0083044 s, mytime2: 0.0029063 s
Number of perms for n = 7: 5040.
For n = 7: pytime: 0.0012613 s,  mytime1 = 0.009655 s, mytime2: 0.0227071 s
Number of perms for n = 8: 40320.
For n = 8: pytime: 0.011169 s,  mytime1 = 0.0824176 s, mytime2: 0.1662243 s
Number of perms for n = 9: 362880.
For n = 9: pytime: 0.1020929 s,  mytime1 = 1.0273658 s, mytime2: 2.463884 s
Number of perms for n = 10: 3628800.
For n = 10: pytime: 0.6239962 s,  mytime1 = 9.2568664 s, mytime2: 19.1452197 s
'''

# Print function to test while debugging.
def myprint(perm):
    for i in range(0,len(perm)):
        print(f"{perm[i]}, ", end = " ")
    input("Press enter to continue.")

# generator function will take input of int n and generate and return a list of all permutations of {1,2,...,n}
def generator(n):
    perm = [None for i in range(1,n+1)]
    for i in range(0,n):
        perm[i] = Digit(i+1)
    permArr = []
    permArr.append(perm)
    while (True):
        max, maxindex = maxmobile(permArr[-1])
        if (maxindex == None):
            break
        permToAdd = nextperm(permArr[-1], max, maxindex, n)
        permArr.append(permToAdd)
    return permArr

def updateDirections(perm, max):
    for element in perm:
        if (element > max):
            element.updateDir()
    return perm


def nextperm(perm, max, maxindex, n):
    if (max.dir == "Left"):
        perm[maxindex-1], perm[maxindex] = perm[maxindex], perm[maxindex-1]
    else:
        perm[maxindex+1], perm[maxindex] = perm[maxindex], perm[maxindex+1]

    if max.digit < n:
        perm = updateDirections(perm,max)
    return perm
    

# Determines max mobile int
def maxmobile(perm):
    max = Digit(0)
    maxindex = None
    permlen = len(perm)
    for i in range(0,permlen):
        if (perm[i].dir == "Left" and (i != 0) and perm[i]>perm[i-1]):
            if perm[i]>max:
                max = perm[i]
                maxindex = i
        elif (perm[i].dir == "Right" and (i != permlen - 1) and perm[i]>perm[i+1]):
            if perm[i]>max:
                max = perm[i]
                maxindex = i

    return max, maxindex



class Digit:
    def __init__(self, value, dir = "Left"):
        self.digit = value
        self.dir = dir
    
    # Function will switch direction of arrow associated with digit
    def updateDir(self):
        if (self.dir == "Left"):
            self.dir = "Right"
        else:
            self.dir = "Left"
    # Function so that when you print an instance of the class, it print the value of digit.
    def __str__(self) -> str:
        return str(self.digit)
    def __lt__(self, other):
        if (self.digit < other.digit):
            return True
        else:
            return False
    def __le__(self, other):
        if (self.digit <= other.digit):
            return True
        else:
            return False 
    def __gt__(self, other):
        if (self.digit > other.digit):
            return True
        else:
            return False
    def __ge__(self, other):
        if (self.digit >= other.digit):
            return True
        else:
            return False 
    def __eq__(self, other):
        if (self.digit == other.digit):
            return True
        else:
            return False
    def __ne__(self, other):
        if (self.digit != other.digit):
            return True
        else:
            return False

if __name__ == "__main__":
    main()