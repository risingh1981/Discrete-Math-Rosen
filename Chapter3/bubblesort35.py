# Chapter 3, Computer Project 5: Given a list of n integers, sort them using a bubble sort.
# Algorithm Summary: Basically, repeatedly swapping adjacent elements if out of order.
# Loop:
# 1) Move from left to right swapping out of order elements, documenting if any swaps made.
# 2) If moved from left to right and no swaps made, then sorted so stop loop.
from random import shuffle
from time import perf_counter_ns

def main():
    # Generate list of randomly ordered ints.
    nums = list(range(1,10000))
    shuffle(nums)
    # Create 2 copies of List nums for Bubblesort function and Python sort function for timing
    numsBS = nums.copy()
    numsPy = nums.copy()
    # Python function to sort list in place. I believe Python uses Timsort algorithm for sorting
    # Note: sorted(list) returns sorted list to be saved in new variable. list.sort() will sort list itself.
    start = perf_counter_ns()
    numsPy.sort()
    end = perf_counter_ns()
    timePy = end - start
    # Bubblesort Function
    numsBS, timeBS = bubblesort(numsBS)
    # Check if sorting worked:
    print(f"Both sorted: {numsBS == numsPy}")
    # Print Time Elapsed
    print(f"List size: {len(nums)}")
    print(f"Python Sort Function: {timePy} nanoseconds.")
    print(f"Bubble Sort Function: {timeBS} nanoseconds.")
    """
    List size: 9999
    Python Sort Function: 1442900 nanoseconds.
    Bubble Sort Function: 30980010700 nanoseconds.
    """


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
