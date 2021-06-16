# This program will determine whether Zn is cyclic and for which values it is cyclic.

def main():
    # Choose value for n in Zn
    n = 17
    # Generate Dictionary
    generators = {}
    values = {}
    keys = range(1,n)
    for i in keys:
        generators[i] = True

    # Check each value to see if it generates all of Z.
    # keys has values 1 - (n-1)
    for i in keys:
        for p in keys:
            values[p] = None
        for t in range(1,n):
            values[(i ** t) % n] = True
        #print (f"For Generator {i} : {values}")
        for key, value in values.items():
            if (value == None):
                generators[i] = False
                break

    cyclic = any(value == True for value in generators.values())
    
    print("Generators: ",generators)
    print(f"Z{n} %s cyclic." %("is" if cyclic else "is not"))
    


if __name__ == "__main__":
    main()