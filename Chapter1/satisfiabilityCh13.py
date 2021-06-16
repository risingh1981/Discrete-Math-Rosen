# Chapter 1, Computer Project 3: Given a compound proposition in CNF form, determine whether it is satisfiable
# by checking its truth value for all possible assignments
# of truth values to its propositional variables.
'''
Index: [90, 221729]
Time(secs) Total: 28049.61047 in Bin:392.1416217 in CTV:27205.5665667 in SAT:451.9022816
Total time in minutes: 467.49350783333335
'''

import sys
import time

def main():
    # n = number of variables
    # clauses =["1 -2 3", " 1 2 3 ", "-1 -2 -3"]
    # (a ∨ ¬b ∨ ¬c ∨ d) ∧ (¬a ∨ d) ∧ (b ∨ e)
    # a = 1 b =2 c = 3 d = 4 e = 5
    # clauses = ["1", "-1"]
    # (x∨y∨z)∧(x∨y∨¬z)∧(x∨¬y∨z)∧(x∨¬y∨¬z)∧(¬x∨y∨z)∧(¬x∨y∨¬z)∧(¬x∨¬y∨z)∧(¬x∨¬y∨¬z)
    #clauses = ["1 2 3","1 2 -3","1 -2 3", "1 -2 -3", "-1 2 3","-1 2 -3","-1 -2 3","-1 -2 -3"]
    """
    clauses = ["1 -2 -3 4","-1 4", "2 5"]
    n = 5
    """
    filename = "cnf1.txt"
    clauses, n = processfile(filename)
    n = int(n)
    
    

    clauses = split(clauses)
    print("Clauses after split: ", clauses)
    
    trialboolvalues, totalBin = binary(n)
    #print("Trial bool values: ", trialboolvalues) # [[False, False, False], [False, False, True], [False, True, False], 
    # [False, True, True], [True, False, False], [True, False, True], [True, True, False], [True, True, True]]
    clausaltruthvalues, totalCTV = clausestruthvalues(clauses,trialboolvalues)
    #print("Clausal Truth Values:")
    #print(clausaltruthvalues)
    sat, index, totalSat = satisfiable(clausaltruthvalues)
    total = totalBin + totalCTV + totalSat
    totalmins = total/60
    print(f"Satisfiable: {sat}")
    print(f"Index: {index}")
    print(f"Time(secs) Total: {total} in Bin:{totalBin} in CTV:{totalCTV} in SAT:{totalSat}")
    print(f"Total time in minutes: {totalmins}")
    # Remaining: 134.403 was the number for clausestruthvalues when i:1 Max i:91 j:1048576
    #Time: 8:05 AM started about 10 mins prior


    # Determine satisfiability
    #sat = satisfiable(clausaltruthvalues)


# Will determine final satisfiability based on the truthvalues for the clauses for all combinations of truth values.
def satisfiable(clausaltruthvalues):
    sat = False
    index = []
    start = time.perf_counter_ns()
    timer = False
    for i in range(0, len(clausaltruthvalues[0])): # 0 - 7
        if (sat == True):
            break
        if (i == 1):
            end1 = time.perf_counter_ns()
            elapsed = (end1 - start) / (10 ** 9)
            timer = True
        for j in range(0, len(clausaltruthvalues)): # 0 -2
            if (timer):
                print(f"Satisfiability(): On i:{i} j:{j} Max i:{len(clausaltruthvalues[0])} Max j:{len(clausaltruthvalues)} Remaining(s):{(len(clausaltruthvalues[0])-i)*elapsed}")
            if (clausaltruthvalues[j][i] == False):
                break
            if (j == len(clausaltruthvalues) - 1):
                 sat = True
                 index.append(j)
                 index.append(i)
    end2 = time.perf_counter_ns()
    total = (end2 - start) / (10 ** 9)
    return sat, index, total

# To get input from file of clauses. Returns clauses array and number of variables.
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

# Function will return an array containing subarrays for the possible truth values.  The elements of the subarrays 
# represent the truth value of each clause for each possible combination of truth values
def clausestruthvalues(clauses, trialboolvalues):
    truthvaluesforclauses = []
    start = time.perf_counter_ns()
    timer = False
    for i in range(0,len(clauses)):
        clause = clauses[i]
        trialarray = [False] * len(trialboolvalues)
        if (i == 1):
            end1 = time.perf_counter_ns()
            elapsed = (end1 - start)/(10 ** 9)
            timer = True
             
        for j in range(0,len(trialboolvalues)):
            if (timer):
                print(f"Clausestruthvalues() On i:{i} j:{j} Max i:{len(clauses)} Max j:{len(trialboolvalues)} Remaining:{(len(clauses)-i)*elapsed}")
            foundtruevar = False
            for var in clause:
                if (foundtruevar == True):
                    break
                varbeingchecked = int(var)
                #print(f"i:{i} j:{j} varbeingchecked:{varbeingchecked}")
                #print(trialboolvalues)
                if ((varbeingchecked > 0) and trialboolvalues[j][varbeingchecked - 1]):                 
                    trialarray[j] = True
                    foundtruevar = True
                    break
                elif ((varbeingchecked < 0) and not(trialboolvalues[j][abs(varbeingchecked) - 1])):
                    trialarray[j] = True
                    foundtruevar = True
                    break
        truthvaluesforclauses.append(trialarray)
    end2 = time.perf_counter_ns()
    total = (end2 - start)/(10 ** 9)
    return truthvaluesforclauses, total
                

# Generate clauses array in proper format. ie. [[1 2 3],[-1 -2 3],[1 -2 -3]]
def split(clauses):
    for i in range(len(clauses)):
        clauses[i] = clausetoarray(clauses[i])
    return clauses

# Helper function for split().Convert a single clause string to array by splitting at white spaces. Return array.
def clausetoarray(clause):
    i = 0
    clause = clause.strip()
    clausearray = []
    str = ""
    for i in range(0,len(clause)):
        if (clause[i] == " "):
            clausearray.append(str)
            str = ""
            continue
        str = str + clause[i]
        if (i == len(clause) - 1):
            clausearray.append(str)
    return clausearray

# Generates an array of arrays of possible T/F values for each of n propositional variables.
def binary(n):
    max = 2 ** n
    binarray = []
    start = time.perf_counter_ns()
    timer = False
    for i in range(0,max):
        if (i == 50000):
            end = time.perf_counter_ns()
            timer = True
            first50 = (end - start) / (10 ** 9)
            #expectedsec = int((max / 50000) * first50)
            #expectedmin = round(expectedsec / 60, 2)
        if (timer):
            print(f"Function: Binary() Max is : {max}. Currently working on: {i} Remaining time(s): {round((max - i)*(first50/50000),2)}")
        else:
            print(f"Max is : {max}. Currently working on: {i}")
        binarray.append(splitbin(padding(bin(i)[2:],n)))
    endBin = time.perf_counter_ns()
    total = (endBin - start)/(10 ** 9)
    return binarray, total
# Helper function for binary() function:
# To convert each possible binary sequence to appropriate True/False values
def splitbin(bin):
    splitbinarray = []
    for char in bin:
        if (char == "0"):
            splitbinarray.append(False)
        else:
            splitbinarray.append(True)
    return splitbinarray

# Helper function for binary() function.
# Will pad the binary string with zeros to make length equal to number of variables in proposition
def padding(str, n):
    str = "0" * (n - len(str)) + str
    return str



if __name__ == "__main__":
    main()
