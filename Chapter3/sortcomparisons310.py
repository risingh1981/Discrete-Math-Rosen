# Chapter 3, Computer Project 10: Given a list of integers, determine the number of comparisons
# used by the bubble sort and by the insertion sort to
# sort this list.
from random import shuffle


def main():
    # Generate list of randomly ordered ints.
    nums = list(range(1,10001))
    shuffle(nums)
    # Create 2 copies of List nums for Insertion Sort Function & Bubblesort function.
    numsIS = nums.copy()
    numsBS = nums.copy()

    # Bubblesort Function:
    numsBS, comparisonsBS = bubblesort(numsBS)
    # Insertionsort Function:
    numsIS, comparisonsIS = insertionsort(numsIS)

    # Comparisons:
    print(f"List size: {len(nums)}")
    print(f"Insertion Sort Function: {comparisonsIS}.")
    print(f"Bubble Sort Function: {comparisonsBS}.")

    # Results:
    '''
    List size: 999
    Insertion Sort Function: 486988.
    Bubble Sort Function: 747531.

    List size: 10000
    Insertion Sort Function: 49657648.
    Bubble Sort Function: 73501350.

    '''
    # Insertion sort: O(n^2) 
    # Bubble sort:  O(n^2)


def bubblesort(numsBS):
    comparisons = 0
    notsorted = True
    while(notsorted):
        notsorted = False
        for i in range(len(numsBS)-1):
            if (not((numsBS[i] > numsBS[i+1]))):
                comparisons += 1
            if (numsBS[i] > numsBS[i+1]):
                numsBS[i],numsBS[i+1] = numsBS[i+1],numsBS[i]
                notsorted = True
    return numsBS, comparisons

def insertionsort(numsIS):
    comparisons = 0
    for i in range(1,len(numsIS)):
        key = numsIS[i]
        j = i - 1
        if (not((j>=0) and (key < numsIS[j]))):
            comparisons += 2
        while ((j>=0) and (key < numsIS[j])):
            numsIS[j+1] = numsIS[j]
            j -= 1
            comparisons += 2
        numsIS[j+1] = key
    return numsIS, comparisons

if __name__ == "__main__":
    main()