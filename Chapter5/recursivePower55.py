# Chapter 5, Problem 5: Given a real number a and a nonnegative integer n, find
# a^n using recursion.

def main():
    # Input: A = real number, p = non-negative power to take A to.
    a = 2
    p = 3

    # Output
    print(power(a,p))

def power(num, pow):
    # Recursive Base Case
    if (pow == 1):
        return num

    return num * power(num, pow - 1)






if __name__ == "__main__":
    main()