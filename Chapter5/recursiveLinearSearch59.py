# Chapter 5, Problem 9: Given a list of integers and an element x, locate x in this
# list using a recursive implementation of a linear search.

def main():
    # Input: List of Integers and element x to search for.
    nums = list(range(20))
    x = 19

    # Output
    print(recursiveLinearSearch(nums,x))
   
    
# This function use a helper recursive function to recursively linear search 
# list nums for value x. If found, returns index of x, otherwise returns None.
def recursiveLinearSearch(nums,x):
    # Call function rlsHelper() to do recursive linear search.
    index = rlsHelper(nums,x)
    # Return None if index = len(nums) or return index
    return (None if (index == len(nums)) else index)
    
# Recursive Linear Search function. Returns index of value x in List nums, or 
# returns len(nums) if value  x not found.
def rlsHelper(nums, x):
    # Recursive Base Cases
    if(len(nums) == 0):
        return 0
    elif (nums[0] == x):
        return 0
    # Recursive Call
    return 1 + rlsHelper(nums[1:],x)    


if __name__ == "__main__":
    main()