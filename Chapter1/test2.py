def main():
    clauses, variables = processfile("cnf1.txt")
    print(clauses, variables)

def processfile(filename):
    clauses =[]
    start = False
    count = 1

    # open the file for reading
    filehandle = open(filename, 'r')
    while True:
        # read a single line
        line = filehandle.readline()
        if not line:
            break
        line = line.strip()
        if (line[-1:] == "0"):
            line = line.strip()[:-2]
        if (start == True):
            clauses.append(line)
        if (bool(line) and line[0] == "p"):
            start = True
            variables = line.split(' ')[2]
            numclauses = line.split(' ')[4]
            
    # close the pointer to that file
    filehandle.close()
    return clauses, variables

if __name__ == "__main__":
    main()