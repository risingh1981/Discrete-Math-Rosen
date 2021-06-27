# Chapter 5, Problem 7: Given a real number a and a nonnegative integer n, 
# find a^n using the binary expansion of n and a recursive algorithm
# for computing a^(2^k).

def main():
    # Input: A = real number, n = power to which to take a to.(ie a^n)
    a = 3
    n = 10

    # Output
    print(powBinExp(a,n))

    
    
def powBinExp(a, n):
    binary = bin(n)
    total = 1
    for index in range(2,len(binary)):
        if (binary[index] == "1"):
            total = total * power2n(a, len(binary) - index - 1)          
    return total
    

def power2n(num, pow):   
    return power(num, power(2,pow))

def power(num, pow):
    if (pow == 0):
        return 1
    return num * power(num, pow - 1)


if __name__ == "__main__":
    main()