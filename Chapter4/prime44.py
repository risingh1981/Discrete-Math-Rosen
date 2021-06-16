from math import *

def main():

    n = int(input("What number would you like to check for primality? "))
    root = int(sqrt(n))
    prime = True
    for i in range(2, root + 1):
        if (n % i == 0):
            print(f"The number {n} is composite")
            prime = False

    if (n == 1):
        print("The number 1 is neither prime or composite.")
    elif (prime):
        print(f"The number {n} is prime.")


if __name__ == "__main__":
    main()