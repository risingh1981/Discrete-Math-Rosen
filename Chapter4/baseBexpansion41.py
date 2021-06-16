def main():
    # Set b equal to the base you want the expansion in. Program works upto base 35.
    b = 35
    # Set n equal to number you want to convert to base b.
    n = 367787685
    print(convert(n,b))

'''
Algorithm: For number n and base b: express # as: n = bq + r1. On each iteration,
save value of r1 in string. Repeat with eq. q = b*q2 + r2. Save r2 in string.
Repeat till q(n) is zero and add r(n) to string. String will be r(n),...r2,r1.
'''
def convert(n,b):
    letters = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F", 16:"G", 17:"H", 18:"I", 19:"J", 20:"K", 21:"L", 22:"M", 23:"N", 24:"O", 25:"P", 26:"Q", 27:"R", 28:"S", 29:"T", 30:"U", 31:"V", 32:"W", 33:"X", 34:"Y", 35:"Z"}
    baseb = ""
    while (n != 0):
        r = n % b
        n = int(n/b)
        if (r > 9):
            baseb = letters[r] + baseb
        else:
            baseb = str(r) + baseb

    return baseb

if __name__ == "__main__":
    main()



