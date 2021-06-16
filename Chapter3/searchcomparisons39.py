# Chapter 3, Computer Project 9: Given an ordered list of n integers and an integer x in the
# list, find the number of comparisons used to determine
# the position of x in the list using a linear search and using
# a binary search.

def main():
    # Input range of ints to generate:
    n = 10000
    # Input the number "x", you would like  to search for:
    x = 500
    # Generate List of numbers 1 through n and shuffle.
    ints = list(range(1,n))

    # Call Binary and Linear Search on list ints.
    indexBS, comparisonsBS = binarysearch(ints,x)
    indexLS, comparisonsLS = linearsearch(ints,x)

    # Output Number of Comparisons per Search Algorithm:
    print(f"Value searched for:{x}. Total values in list:{n-1} and Number of Comparisons:")
    print(f"Binary Search: Index={indexBS}  Comparisons:{comparisonsBS}")
    print(f"Linear Search: Index={indexLS}  Comparisons:{comparisonsLS}")
    
    #Results 
    '''
    Value searched for:9999. Total values in list:9999 and Number of Comparisons:
    Binary Search: Index=9998  Comparisons:27
    Linear Search: Index=9998  Comparisons:9999

    Value searched for:5. Total values in list:9999 and Number of Comparisons:
    Binary Search: Index=4  Comparisons:25
    Linear Search: Index=4  Comparisons:5

    Value searched for:500. Total values in list:9999 and Number of Comparisons:
    Binary Search: Index=499  Comparisons:25
    Linear Search: Index=499  Comparisons:500
    '''

def binarysearch(ints,p):
    b = 0 
    e = len(ints)-1
    comparisons = 0
    while True:
        m = (b + e)//2
        if (p == ints[m]):
            comparisons +=1
            return m, comparisons
        elif (p > ints[m]):
            comparisons += 2
            b = m + 1
        else: # (p<ints[m])
            comparisons += 2
            e = m - 1
    # If p not found in list ints, return none
    return None

def linearsearch(ints,p):
    comparisons = 0
    for i in range(len(ints)):
        comparisons += 1
        if (ints[i] == p):
            return i, comparisons
    return None, comparisons

if __name__ == "__main__":
    main()