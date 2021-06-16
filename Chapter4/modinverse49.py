def main():
    # Given relatively prime positive integers a and b, find an
    # inverse of a modulo b. Since a,b relatively prime -> gcd(a,b) = 1 -> inverse exists.
    a = 3379
    b = 4061
    print(f"Inverse of {a} (mod {b}) is {inverse(a,b)}.")

# Returns inverse of a mod b, if it exists.
def inverse(a,b):
    if (gcd(a,b) != 1):
        print(f"{a} (mod {b}) does not have an inverse since GCD({a},{b}) is not equal to 1.")
        return
    for i in range(1,b):
        if (a*i % b == 1):
            return i
        

def gcd(a,b):
    for i in range(min(a,b), 0, -1):
        if (a % i == 0) and (b % i == 0):
            return i

if __name__ == "__main__":
    main()