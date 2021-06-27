# 6k +- 1 Primality Test

def main():
    # nums = [1,3,17,257,25,19,100,104729]
    nums = [20576131]
    
    for i in range(0, len(nums)):
        print(f"Number: {nums[i]}  Prime: {prime(nums[i])}")

def prime(n):   
    if (n <= 3):
        return (n > 1)
    if (n % 2 == 0) or (n % 3 == 0):
        return False
    # This part uses fact that all numbers can be represented in form 6k + x, where k is an int => 0 
    # and x = {0,1,2,3,4,5}. Multiples of 6k + {0,2,3,4} already rules out above. Just have to check
    # multiples of 6k - 1 and 6k + 1 less than sqrt(n).
    i = 5 # Initial value is 6(1) - 1 = 5 and 6(1) + 1 = 7
    while (i ** 2 <= n):
        if (n % i == 0) or (n % (i+2)) == 0:
            return False
        i += 6
    return True

if __name__ == "__main__":
    main()