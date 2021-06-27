# Chapter 5, Problem 6: Given a real number a and a nonnegative integer n, find
# a^(2^n) using recursion.
def main():
    # Input: A = real number, p = power of 2 to take a to.(ie a^2^p)
    a = 3
    p = 4

    # Output
    print(power2n(a,p))

def power2n(num, pow):   
    return power(num, power(2,pow))

def power(num, pow):
    if (pow == 1):
        return num
    return num * power(num, pow - 1)


if __name__ == "__main__":
    main()