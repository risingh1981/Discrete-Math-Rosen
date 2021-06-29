# Chapter 6, Computer Project 9: Given positive integers n and r, list all the 
# r-permutations, with repetition allowed, of the set {1, 2, 3, . . . , n}.
def main():

    # Input
    r = 3
    n = 5
    inputArr = [x for x in range(1,n+1)]

    # Output
    print(rpermswithrep(inputArr, r))
    

def rpermswithrep(inputArr, r):
    n = len(inputArr)
    perm = []
    outputArr = []
    rpermswithrepRec(inputArr, outputArr, perm, n, r)
    return outputArr
 

def rpermswithrepRec(inputArr, outputArr, perm, n, r): 
    # Base case
    if (r == 0) :
        outputArr.append(perm)
        return
    for i in range(n):
        newperm = perm + [inputArr[i]]
        rpermswithrepRec(inputArr, outputArr, newperm, n, r - 1)



if __name__ == "__main__":
    main()


