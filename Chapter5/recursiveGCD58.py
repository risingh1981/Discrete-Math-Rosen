# Chapter 5, Problem 8: Given two integers not both zero, find their greatest 
# common divisor using recursion.

def main():
    # Input: 2 int(not both 0) to find GCD of
    a = 20
    b = 15

    # Output
    print(recursiveGCD(a,b))
    

def recursiveGCD(a,b):
    if ((a == 0) or (b == 0)):
        return max(abs(a),abs(b))
    # Calculate Remainder:
    r = a % b
    # Recursive Base Case:
    if (r == 0):
        return abs(b)
    # Recursive Call
    return recursiveGCD(b, r)


    
    


if __name__ == "__main__":
    main()