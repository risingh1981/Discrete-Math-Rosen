# Chapter 3, Computer Project 6: Given a list of n integers, sort them using an insertion
# sort.
# Algorithm Summary for Insertion Sort:
# 1) Array is split into sorted and unsorted part.
# 2) Values from unsorted part placed into correct spot in sorted part.
# To sort an array of size n in ascending order: 
# 1: Iterate from arr[1] to arr[n] over the array. 
# 2: Compare the current element (key) to its predecessor. 
# 3: If the key element is smaller than its predecessor, compare it to the elements before. Move the greater 
#    elements one position up to make space for the swapped element.
from random import shuffle
from time import perf_counter_ns

def main():
    # Generate list of randomly ordered ints.
    nums = list(range(1,10000))
    shuffle(nums)
    # Create 3 copies of List nums for Insertion Sort Function, Bubblesort function and Python sort function 
    # for timing
    numsIS = nums.copy()
    numsBS = nums.copy()
    numsPy = nums.copy()
    # Python function to sort list in place. I believe Python uses Timsort algorithm for sorting
    # Note: sorted(list) returns sorted list to be saved in new variable. list.sort() will sort list in place.
    start = perf_counter_ns()
    numsPy.sort()
    end = perf_counter_ns()
    timePy = end - start
    # Bubblesort Function
    numsBS, timeBS = bubblesort(numsBS)
    # Insertionsort Function
    numsIS, timeIS = insertionsort(numsIS)
    # Check if sorting worked:
    print(f"Insertion sort worked: {numsIS == numsPy}")
    # Print Time Elapsed
    print(f"List size: {len(nums)}")
    print(f"Insertion Sort Function: {timeIS} nanoseconds.")
    print(f"Python Sort Function: {timePy} nanoseconds.")
    print(f"Bubble Sort Function: {timeBS} nanoseconds.")

    '''
    Results:
    List size: 4
    Insertion Sort Function: 9824200 nanoseconds.
    Python Sort Function: 1700 nanoseconds.
    Bubble Sort Function: 6300 nanoseconds.

    List size: 9999
    Insertion Sort Function: 9129015300 nanoseconds. ~9.129 seconds
    Python Sort Function: 1892900 nanoseconds. ~ 0.0018929 seconds
    Bubble Sort Function: 31272170700 nanoseconds.~ 31.2721707 seconds

    '''


def insertionsort(numsIS):
    start = perf_counter_ns()
    for i in range(1,len(numsIS)):
        key = numsIS[i]
        j = i - 1
        while ((j>=0) and (key < numsIS[j])):
            numsIS[j+1] = numsIS[j]
            j -= 1
        numsIS[j+1] = key
    end = perf_counter_ns()
    timeIS = end - start
    return numsIS, timeIS

def bubblesort(numsBS):
    start = perf_counter_ns()
    notsorted = True
    while(notsorted):
        notsorted = False
        for i in range(len(numsBS)-1):
            if (numsBS[i] > numsBS[i+1]):
                numsBS[i],numsBS[i+1] = numsBS[i+1],numsBS[i]
                notsorted = True
    end = perf_counter_ns()
    timeBS = end - start
    return numsBS, timeBS


if __name__ == "__main__":
    main()