# Chapter 3, Computer Problem 4: Given an ordered list of n distinct integers, determine the
# position of an integer in the list using a binary search.
# Added additional time measurements to compare functions and pythons built-in index function.
import time

def main():
    # Input range of ints to generate:
    n = 10000
    # Input the number you would like  to search for
    p = 9999
    # Generate List of numbers 1 through n and shuffle.
    ints = list(range(1,n))
    
    # Call function linearsearch(<list>,p). Functions returns index and time in nanoseconds to search.   
    indexbs,bstime = binarysearch(ints,p)
    # Time Pythons built in index function:
    start = time.perf_counter_ns()
    indexpy = ints.index(p)
    end = time.perf_counter_ns()
    pytime = end - start
    # Time Linear Search
    indexls,lstime = linearsearch(ints,p)
    # Output
    print(f"Per binary search function, the index of {p} in generated list is:{indexbs}, Time: {bstime}")
    print(f"Per linear search function, the index of {p} in generated list is:{indexls}, Time: {lstime}")
    print(f"Per Pythons built-in index function, the index of {p} is {indexpy}. Time: {pytime}")
    # Time Results on Ordered List of ints 0-9999 with mentioned search values:
    # List(1,...,9999), Search for 8600:Binary Search: 7000 ns < Pythons Index Function: 202,000 ns < Linear Search: 933800 ns
    # List(1,...,9999), Search for 1:Pythons Index Function: 1600 ns < Linear Search: 2000 ns < Binary Search: 6300 ns 
    # List(1,...,9999), Search for 9999:Binary Search: 6900 ns < Linear Search: 1089100 ns < Pythons Index Function: 239900 ns <

# Function returns index of int p in list ints. If p is not found, it returns None.
def binarysearch(ints,p):
    start = time.perf_counter_ns()

    b = 0 
    e = len(ints)-1
    #print(f"b: {b} e:{e}")
    while True:
        m = (b + e)//2
        #print(f"recalculated m: {m}. b:{b}, e:{e}")
        if (p == ints[m]):
            end = time.perf_counter_ns()
            #input(f"p:{p} == ints[{m}]:{ints[m]}. found, about to return from function")
            return m, (end - start)
        elif (p > ints[m]):
            #input(f"p:{p} > ints[{m}]:{ints[m]}. not found, about to change b({b}) to (m + 1)({m+1})")
            b = m + 1
        else: # (p<ints[m])
            #input(f"p:{p} < ints[{m}]:{ints[m]}. not found, about to change e:({e}) to (m):({m -1})")
            e = m - 1
    # Int p not found in list ints:
    end = time.perf_counter_ns()
    return None, (end - start)


# Function returns index of int p in list ints. If p is not found, it returns None.
def linearsearch(ints,p):
    start = time.perf_counter_ns()
    for i in range(len(ints)):
        if (ints[i] == p):
            end = time.perf_counter_ns()
            return i, (end - start)
    return None, (end - start)

    

if __name__ == "__main__":
    main()