# Chapter 1 Computer Project 2: Given two bit strings of length n, find the bitwise AND,
# bitwise OR, and bitwise XOR of these strings.

def main():
    # Input 2 bitstrings(if unequal in size, the smaller string will be counted as an equal len string 
    # with leading zeros added)
    bs1 = "011101"
    bs2 = "0111"
    
    # Print bitwise AND of bs1 abd bs2
    print(bitand(bs1,bs2))
    # Print bitwise OR of bs1 abd bs2
    print(bitor(bs1,bs2))
    # Print bitwise XOR of bs1 abd bs2
    print(bitxor(bs1,bs2))


# Function for bitwise AND
def bitand(str1, str2):
    str3 = bin(int(str1,2 ) & int(str2, 2))[2:]
    return padding(str1, str2, str3)

# Function for bitwise OR
def bitor(str1, str2):
    str3 = bin(int(str1,2) | int(str2, 2))[2:]
    return padding(str1, str2, str3)

# Function for bitwise XOR
def bitxor(str1, str2):
    str3 = bin(int(str1,2) ^ int(str2, 2))[2:]
    return padding(str1, str2, str3)

# Will determine if leading zeros need to be added to bit strings and will add it necessary.
def padding(str1, str2, str3):
    if ((max(len(str1),len(str2))) > len(str3)):
        str3 = "0" * ((max(len(str1),len(str2))) - len(str3)) + str3
    return str3


if __name__ == "__main__":
    main()