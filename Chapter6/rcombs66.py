# Chapter 6, Computer Project 6: Given a positive integer n and a nonnegative integer r
# not exceeding n, list all the r-combinations of the set {1, 2, 3, . . . , n} in lexicographic order.  


def main():
    # Input
    n = 3
    r = 1
    # Generate input arr
    inputArr = [x for x in range(1, n + 1)]
    

    # Output
    answer = rcombs(inputArr, r)
    print(answer)

    
# Rosen: Algorithm for generating the r-combinations of the set {1, 2, 3, . . . , n} in lexicographic order.
# An r-combination can be represented by a sequence containing the elements in the subset in increasing 
# order. In this lexicographic ordering, the first r-combination is {1, 2, . . . , r − 1, r}
# and the last r-combination is {n − r + 1, n − r + 2, . . . , n − 1, n}.
# The next r-combination after a1a2 · · · ar can be obtained in the following way:
# 1) Locate the last element ai in the sequence such that ai ≠ n − r + i.
# 2) Replace ai with ai + 1 and aj with ai + j − i + 1, for j = i + 1, i + 2, . . . , r.
def rcombs(inputArr, r):
    rcombsArr = [[x for x in range(1,r+1)]]
    lastrcomb = inputArr[-r:]
    n = len(inputArr)
 
    while(rcombsArr[-1] != lastrcomb):
        newrcomb = nextcomb(rcombsArr[-1],r,n)
        rcombsArr.append(newrcomb.copy())
    return rcombsArr

# Generates next r-combinations in lexicographic order from input r-combination:rcomb.
def nextcomb(rcomb, r, n):
    newrcomb = rcomb.copy()
    r = r - 1
    n = n - 1
    i = r
    while (newrcomb[i] == n - r + i + 1):
        i = i - 1
    newrcomb[i] = newrcomb[i] + 1
    for j in range(i+1,r+1):
        newrcomb[j] = newrcomb[i] + j - i
    return newrcomb



if __name__ == "__main__":
    main()