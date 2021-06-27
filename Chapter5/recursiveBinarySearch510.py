# Chapter 5, Problem 10: Given a *sorted* list of integers and an element x, locate x in this
# list using a recursive implementation of a binary search.

def main():
    # Input: List of Integers and element x to search for.
    nums = list(range(20))
    x = 13

    # Output
    print(recursiveBinarySearch(nums,x))
   
    
# This function use a helper recursive function to recursively binary search 
# sorted list nums for value x. If found, returns index of x, otherwise returns None.
def recursiveBinarySearch(nums,x):
    # Call rbsHelper function with parameters: name of list, start index = 0, 
    # end index = len(nums)-1, and value being searched for.
    if (x < nums[0]) or (x > nums[len(nums) - 1]):
        return None
    else:
        return rbsHelper(nums, 0, len(nums) - 1, x)
    
# Recursive Linear Search function. Returns index of value x in List nums, or 
# returns len(nums) if value  x not found.
def rbsHelper(nums, start, end, x):
    mid = (start + end) // 2
    # Recursive Base Cases
    if (nums[mid] == x):
        return mid
    elif (start == end):
        return None
    # Recursive Calls
    if (x > nums[mid]):
        return rbsHelper(nums, mid + 1, end, x)
    else:
        return rbsHelper(nums, start, mid - 1, x)  


if __name__ == "__main__":
    main()