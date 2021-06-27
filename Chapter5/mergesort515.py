# Chapter 5, Problem 15: Given a list of n integers, sort these integers using 
# the merge sort.
from random import shuffle
from time import perf_counter_ns
from DiscreteMathRosen.Chapter3.bubblesort35 import bubblesort
from geeksms import mergeSort


def main():
    # Generate list of randomly ordered ints.
    nums = list(range(1,10000))
    shuffle(nums)
    # Create 4 copies of List nums for Bubblesort function and Python sort function for timing
    numsMS = nums.copy() # MergeSort
    numsPy = nums.copy() # Python built-in function
    numsBS = nums.copy() # Bubble sort
    numsGKG = nums.copy() # Geeks for Geeks mergesort Algo
    # Python function to sort list in place. I believe Python uses Timsort algorithm for sorting
    # Note: sorted(list) returns sorted list to be saved in new variable. list.sort() will sort list itself.
    start = perf_counter_ns()
    numsPy.sort()
    end = perf_counter_ns()
    timePy = end - start
    # Mergesort Function
    start = perf_counter_ns()
    numsMS = mergesort(numsMS)
    end = perf_counter_ns()
    timeMS = end - start
    
    # Geeks for Geeks MergeSort Algo
    start = perf_counter_ns()
    n = len(numsGKG)
    mergeSort(numsGKG,0,n-1)
    end = perf_counter_ns()
    timeGKG = end - start

    # Bubblesort Function
    numsBS, timeBS = bubblesort(numsBS)
    # Check if sorting worked:
    print(f"Did algo sort?: {numsMS == numsPy}")
    
    # Print Time Elapsed
    print(f"List size: {len(nums)}")
    print(f"Python Sort Function: {timePy} nanoseconds.")
    print(f"Merge Sort Function: {timeMS} nanoseconds.")
    print(f"Bubble Sort Function: {timeBS} nanoseconds.")
    print(f"Merge Sort GKG Function: {timeGKG} nanoseconds.")

    '''
    Both sorted?: True
    List size: 9999
    Python Sort Function: 1317000 nanoseconds.
    Merge Sort Function: 39505000 nanoseconds.
    Bubble Sort Function: 12847249500 nanoseconds.
    
    Both sorted?: True
    List size: 9999
    Python Sort Function: 1293300 nanoseconds.
    Merge Sort Function: 42525800 nanoseconds.
    Merge Sort GKG Function: 63765200 nanoseconds.
    '''
    

def mergesort(nums):
    # Mergesort helper function so user does not have to pass beginning and ending
    # indices. Will be checked in  this function and passed to msHelper.
    if (len(nums) == 0):
        return nums
    start = 0
    end = len(nums) - 1
    return msHelper(nums,start,end)

def msHelper(nums, start, end):
    mid = (start + end) // 2
    if (start == end):
        return [nums[start]]
    return merge(msHelper(nums,start, mid),msHelper(nums,mid + 1, end))

def merge(A,B):
    result = []
    lenA = len(A)
    lenB = len(B)
    indexA = 0
    indexB = 0
    for i in range(0, lenA + lenB):
        if (indexA == lenA):
            result = result + B[indexB:]
            break
        elif (indexB == lenB):
            result = result + A[indexA:]
            break
        if (A[indexA] < B[indexB]):
            result.append(A[indexA])
            indexA += 1
        else:
            result.append(B[indexB])
            indexB += 1
    
    return result

if __name__ == "__main__":
    main()
