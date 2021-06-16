# Compute the check digit when given the first nine digits
# of an ISBN-10.
# Info: ISBNs All books are identified by an International Standard Book Number (ISBN-10), a
# 10-digit code x1x2 . . . x10, assigned by the publisher. An ISBN-10 consists of blocks identifying the 
# language, the publisher, the number assigned to the book by its publishing company, and finally, a check
# digit that is either a digit or the letter X (used to represent 10). This check digit is selected so
# that x10 ≡ (sum from i = 1 to i = 9 of i*xi) mod 11. Digits numbered from left to right. Check digit can
# have value 10, which is represented as "X".


def main():
    # Enter first 9 digits of ISBN:
    #ISBN = "007288008"
    ISBN = "084930149"

    # Calculate check digit:
    x10 = check(ISBN)

    #Output ISBN with appended check digit:
    if (x10 == 10):
        finalISBN = ISBN + "X"
    else:
        finalISBN = ISBN + str(x10)
    print(f"Complete ISBN is: {finalISBN}")

# Check function for ISBN. Returns the check digit of ISBN given first 9 digits.
def check(ISBN):
    i = 1
    sum = 0
    for char in ISBN:
        sum = sum + i*int(char)
        i += 1
    return sum % 11

if __name__ == "__main__":
    main()