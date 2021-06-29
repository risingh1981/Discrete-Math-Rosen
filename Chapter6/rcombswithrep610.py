# Chapter 6, Computer Project 10: Given positive integers n and r, list all the 
# r-combinations, with repetition allowed, of the set {1, 2, 3, . . . , n}.

def main():
    # Input Values
    n = 3
    arr = [x for x in range(1,n+1)]
    r = 2
    # Output
    rcombArr = rcombinationswRep(arr,r)
    print(f"{r}-combinations of {arr}: {rcombArr}")

def rcombinationswRep(arrInput, r):
    # This function will call a helper recursive function that will generate the 
    # r-combinations of the input arr.
    n = len(arrInput) - 1
    rcombsArr = []
    rcomb =[0 for x in range(r)]
    rcombsRecursive(rcombsArr, rcomb, arrInput, 0, r, 0, n)
    return rcombsArr

def rcombsRecursive(rcombsArr, rcomb, arrInput, index, r, start, end):
    if (index == r):
        rcombsArr.append(rcomb.copy())
        return
    if (start > end):
        return

    rcomb[index] = arrInput[start]
    rcombsRecursive(rcombsArr, rcomb, arrInput, index + 1, r, start, end)
    rcombsRecursive(rcombsArr, rcomb, arrInput, index, r, start + 1, end)


if __name__ == "__main__":
    main()
    