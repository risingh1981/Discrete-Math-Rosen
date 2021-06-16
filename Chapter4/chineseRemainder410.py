import numpy
import sys

def main():
    # Prompt user for input
    print("A linear congruence is of the form ax \u2261 b (mod m). This program will solve a system of linear congruences with pairwise relatively prime moduli.")
    print("First input the number of linear congruences in the system and then enter values for a,b, and m for each congruence.")
    n = int(input("How many linear congruences are in your system: "))
    # Initialize arrays for values.
    a = numpy.zeros(n, dtype = int)
    b = numpy.zeros(n, dtype = int)
    m = numpy.zeros(n, dtype = int)
    
    for i in range(1, n + 1):
        print(f"For congruence {i} of form ax \u2261 b (mod m). Enter values for a, b, and m.")
        a[i-1] = int(input("Value of a: "))
        b[i-1] = int(input("Value of b: "))
        m[i-1] = int(input("Value of m: "))
    
    # Save original arrays under another variable as a, b, m will be changed over course of execution of program.
    origA = a.copy()
    origB = b.copy()
    origM = m.copy()
    
    # Check if the system of congruences if solvable and reduce system.
    solvable, na, nb, nm = check(a, b, m)
    
    # Print informational message and Exit program if unsolvable.
    if (solvable == False):
        print("The following system of congruences is unsolvable.")
        for i in range(1, n + 1):
            print(f"Congruence {i}: {origA[i-1]}x \u2261 {origB[i-1]} (mod {origM[i-1]})")
        sys.exit()
    
    # Calculate product of moduli.
    prodm = int(numpy.prod(m))
      
    # Calculate Values for Mk for use with Chinese Remainder Theorem.
    Mk = bigM(m, prodm)

    # Calculate Yk for use in Chinese Remainder Theorem
    Yk = bigY(Mk, m)

    # Calculate final answer to system of congruences.
    x = 0
    for i in range(0,len(a)):
        x = x + b[i]*Mk[i]*Yk[i]
    x = x % prodm

    #Output Solution:
    print("The solution to the following system of linear congruences:")
    for i in range(1, len(origA) + 1):
            print(f"Congruence {i}: {origA[i-1]}x \u2261 {origB[i-1]} (mod {origM[i-1]})")
    print()
    print(f"X \u2261 {x} (mod {prodm})")

# Function calculates Yi (inverse of Mi mod mi) and return array of Yk
def bigY(Mk,m):
    Yk = numpy.zeros(len(m), dtype = int)
    for i in range(0,len(m)):
        Yk[i] = inverse(Mk[i],m[i])
    return Yk

# Returns array of Mi to use in Chinese Remainder Theorem.
def bigM(m, prodm):
    Mk = numpy.zeros(len(m), dtype = int)
    for i in range(0, len(m)):
        Mk[i] = prodm / m[i]
    return Mk

# Function checks for solvability and reduces equation to form usable for Chinese Remainder Theorem.
def check(a,b,m):
    for i in range(0, len(a)):
        if (gcd(a[i],m[i]) == 1):
            b[i] = (b[i] * inverse(a[i],m[i])) % m[i]
            a[i] = 1
    solvable = True
    repeat = True
    while(solvable and repeat):
        for i in range(0, len(a)):
            if ((b[i] % gcd(a[i],m[i])) != 0):
                solvable = False
                print(f"The Equation of form {a[i]} x \u2261 {b[i]} mod {m[i]} is not solvable because GCD({a[i]},{m[i]}) does not divide {b[i]}.")
                break
            gcdaibi = gcd(a[i],b[i])
            gcdaibimi = gcd(gcdaibi, m[i])
            m[i] = m[i] / gcdaibimi
            a[i] = (a[i] / gcdaibi) % m[i]
            b[i] = (b[i] / gcdaibi) % m[i]
            
            if (a[i] > 1):
                repeat = True
                break
            else:
                repeat = False
    return solvable, a, b ,m

# Function to calculates multiplicative inverses in mod b. 
def inverse(a,b):
    if (gcd(a,b) != 1):
        print(f"Program only solves linear congruences with pairwise relatively prime moduli. The system entered requires checking inverse of {a} in {a} mod {b}. {a} and {b} are not relatively prime.")
    for i in range(1,b):
        if (a*i % b == 1):
            return i

#Function to calculate GCD of a and b via Euclidean Algorithm.
def gcd(a,b):
    if (a == 0 and b != 0):
        return b
    elif (b == 0 and a != 0):
        return a
    elif(a == 0 and b == 0):
        print("Attempting to find GCD(0,0).")
    if (a<b):
        a,b = b,a
    if (a % b == 0):
        return b
    return gcd(b, a % b)


if __name__ == "__main__":
    main()