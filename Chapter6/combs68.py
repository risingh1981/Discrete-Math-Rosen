# Chapter 6, Computer Project 8: Given a positive integer n, list all the combinations of the
# set {1, 2, 3, . . . , n}.
# Will use Base 2 Algorithm for generating all the subsets of a set.
from itertools import combinations
from time import perf_counter_ns

def main():
    # Input: Enter value of n for set {1,2,...,n}
    #n = 4
    # Output:
    for n in range(2,16):# Output: 
        # Timing for my function:
        start = perf_counter_ns()
        answer = allcombinations(n)
        end = perf_counter_ns()
        mytime = end - start
    
        # Timing for py combinations function:
        start = perf_counter_ns()
        totArr = []
        arr = [x for x in range(1,n+1)]
        for i in range(1, n+1):
            newcombos = (list(combinations(arr,i)))
            totArr.append(newcombos)
        end = perf_counter_ns()
        pytime = end - start
 
        print(f"For n = {n}, mytime: {mytime} ns,  pytime: {pytime} ns")
        # Timing Results:
        '''
        For n = 2, mytime: 9700 ns,  pytime: 3900 ns
        For n = 3, mytime: 25500 ns,  pytime: 7500 ns
        For n = 4, mytime: 34300 ns,  pytime: 8000 ns
        For n = 5, mytime: 117000 ns,  pytime: 11300 ns
        For n = 6, mytime: 137000 ns,  pytime: 10500 ns
        For n = 7, mytime: 246400 ns,  pytime: 25600 ns
        For n = 8, mytime: 776000 ns,  pytime: 34600 ns
        For n = 9, mytime: 1026600 ns,  pytime: 35100 ns
        For n = 10, mytime: 2822700 ns,  pytime: 140600 ns
        For n = 11, mytime: 5571300 ns,  pytime: 192000 ns
        For n = 12, mytime: 11753300 ns,  pytime: 644300 ns
        For n = 13, mytime: 20200200 ns,  pytime: 863500 ns
        For n = 14, mytime: 45461900 ns,  pytime: 1610100 ns
        For n = 15, mytime: 82681800 ns,  pytime: 6736500 ns
        '''



def allcombinations(n):
    baseSet = [x for x in range(1, n+1)]
    # Generate binary numbers upto 2^n - 1 and store them in list binArr[].
    # (There are 2^n subsets including the empty set.)
    binArr = []
    for i in range(1, 2 ** n):
        binArr.append(bin(i))
    # Create empty list to store all the generated combinations.
    allCombos = [[] for i in range(1,2 ** n)]
    counter = 0
    # Iterate through each binary number in binArr and including the the element in the combo if there
    # is a 1 in the appropriate spot in the binary number.
    for binnumber in binArr:
        lenOfbin = len(binnumber)
        for i in range(lenOfbin-1, 1, -1):
            if (binnumber[i] == "1"):
                eleNum = lenOfbin - i - 1
                allCombos[counter].append(baseSet[eleNum])
        counter += 1
    return allCombos



if __name__ == "__main__":
    main()