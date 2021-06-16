# Given a set of identification numbers, use a hash function
# to assign them to memory locations where there are
# k memory locations.

def main():
    # Enter value for number of memory locations(k):
    k = 10
    # Identification Numbers array:
    ID = [12345,23456,34567,45678,56789,98765,87654,76543,65432,54321]
    # Array Representing k memory locations
    Mem = [None] * k
    # Initialize counter for collisions to zero,
    collisions = 0
    # Assign Values of ID to Memory Locations
    for i in range(0,k):
        memloc = hash(ID[i],k)
     
        if (Mem[memloc] == None):
            Mem[memloc] = ID[i]
        else:
            collisions += 1
            while(Mem[memloc] != None):
                memloc = (memloc + 1) % k
                if (Mem[memloc] == None):
                    Mem[memloc] = ID[i]
                    break
    print(f"Array of Memory Locations: {Mem}")
    print(f"Collisions: {collisions}")


# Using simple division method for hash.
def hash(val, k):
    return (val % k)

if __name__ == "__main__":
    main()
