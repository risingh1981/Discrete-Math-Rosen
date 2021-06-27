# Chapter 5, Problem 11: Given a nonnegative integer n, find the nth Fibonacci
# number using iteration.

def main():
    # Input: Enter value for n. Program will print out fibonacci numbers upto 
    # the nth fibonacci number.
    n = 20

    # Output
    for i in range(0,n):
        print(f"f({i}): {iterativeFibonacci(i)}")
   
    
# Functions returns nth Fibonacci number
def iterativeFibonacci(n):
    #input(f"In IF, value of n ={n}")
    fnMinusTwo = 0
    fnMinusOne = 1
    # If n = 0, returns fnMinusTwo = 0 or if n = 1, returns fnMinusOne = 1
    if (n == 0):
        return fnMinusTwo
    elif (n == 1):
        return fnMinusOne
    # Iterate n - 1 times to find nth Fibonacci Number
    for i in range(1,n):
        temp = fnMinusOne
        fnMinusOne = fnMinusOne + fnMinusTwo
        fnMinusTwo = temp
    # Return nth Fibonacci number which is now stored in fnMinusOne
    #input(f"in IF, about to output fib for n ={n}: {fnMinusOne} ")
    return fnMinusOne

if __name__ == "__main__":
    main()