# Chapter 4, Computer Project 14: Given a message and a positive integer k less than 26,
# encrypt this message using the shift cipher with key k;
# and given a message encrypted using a shift cipher with
# key k, decrypt this message.

def main():
    # String to convert to cipher text:
    plaintext = "This, is a sample !sentence to convert with the cipher. a A z Z"
    # Cipher key(Set k to cipher offset)
    k = 25

    #Test of cipher and decipher function.
    teststr = cipher(plaintext,k)
    print(teststr)
    print(decipher(teststr, k))

def cipher(text, k):
    #Ordinal Values: a:97  z:122  A:65  Z:90
    ct = ""
    for char in text:
        if (char == "a"):
            print(f"Ord of {char}: {ord(char)}")
        if (not ((97 <=ord(char) <= 122) or (65 <= ord(char) <= 90))):
            ct = ct + char
            continue
        if (char.islower()):
            loc = (((ord(char) - 97) + k) % 26) + 97
        else:
            loc = (((ord(char) - 65) + k) % 26) + 65
        if (char == "a"):
            print(f"loc: {loc} chr(loc): {chr(loc)}")
        ct = ct + chr(loc)
    return ct

def decipher(text, k):
    #Ordinal Values: a:97  z:122  A:65  Z:90
    ct = ""
    for char in text:
        if (not ((97 <=ord(char) <= 122) or (65 <= ord(char) <= 90))):
            ct = ct + char
            continue
        if (char.islower()):
            loc = (((ord(char) - 97) - k) % 26) + 97
        else:
            loc = (((ord(char) - 65) - k) % 26) + 65
        ct = ct + chr(loc)
    return ct



if __name__ == "__main__":
    main()