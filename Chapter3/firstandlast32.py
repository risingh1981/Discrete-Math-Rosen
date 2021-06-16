# Chapter 3, Computer Problem 2: Given a list of n integers, find the first and last occurrences
# of the largest integer in the list.

def main():

    # Input: List of n integers.
    n = [1,2,3,49,5,6,49,11,12,14,15,15,7,49,9,10,11] # Max = 49 First Index:3 Last Index:13

    # Output
    largest, firstindex, lastindex = firstlast(n)
    print(f"The largest integer in the list is: {largest}.")
    print(f"The first occurrence of largest integer in list is at index {firstindex} and last occurrence of it at index {lastindex}")

# Function returns 3 values. 1) largest int in list 2) index of first occurrence and 3) last occurrence of largest 
# integer in the list. If largest integer occurs only once, it returns index of largest int for second value 
# and None for the third value.
def firstlast(nums):
    largest = max(nums)
    first = nums.index(largest)
    if (nums.count(largest) == 1):
        return largest, first, None
    else:
        nums.reverse()    
        i = nums.index(largest)
        last = len(nums) - i - 1
        nums.reverse() # Reversing second time to restore nums list to original form. It is faster to reverse
                       # twice than to resort to an algorithm that involves making a copy of the list.
        return largest, first, last


if __name__ == "__main__":
    main()