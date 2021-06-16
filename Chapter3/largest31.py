# Chapter 3, Computer Problem 1: Given a list of n integers, find the largest integer in the
# list.

def main():
    # Input: List of n integers.
    nums = [1,2,3,4,5,6,7,8,9]

    # Output: Largest int in nums
    largest = max(nums)
    print(f"Largest integer in list is: {largest}")

if __name__ == "__main__":
    main()