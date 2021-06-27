# Chapter 6, Program 3: Given a sequence of positive integers, find the longest 
# increasing and the longest decreasing subsequence of the sequence.
# Will use Dynamic Programming(DP) using iterative(tabulation - Bottom Up):
# 2 main properties of a problem that suggest DP's use:
# 1) Overlapping Subproblems & 2) Optimal Substructure
# Overlapping Subproblems - DP mainly used when solutions to the same subproblem used
# again and again. 
# a) Memoization(Top Down)
#    The memoized program for a problem is similar to the recursive version with a small modification that it 
#    looks into a lookup table before computing solutions. Start by breaking largest problem down into smaller 
#    subproblems from top to bottom. If subproblem is solved already, just reuse answer; otherwise, solve 
#    the subproblem and save the result.
# b) Tabulation(Bottom Up)
#    Storing solution for smallest case, and then working way up.
from random import shuffle

def main():
    # Input: Enter values for n and r
    sequence = (list(range(20)))
    shuffle(sequence)
    #sequence = [1,3,2,5,4]
    
    print(sequence)
    # Output: Tuple of longest increasing, decreasing subsequence in sequence entered.
    outputTuple = iterativeLS(sequence)
    print(f"Longest increasing subsequence: {outputTuple[0]}. Longest decreasing subsequence: {outputTuple[1]}.")
    

def iterativeLS(seq):
    seqLen = len(seq)
    # Create array called subseq of length equal to len(seq)to contain tuples. For tuple in subseq[i], first 
    # value in tuple indicates longest increasing subseq ending at seq[i], and second value in tuple indicates
    # longest decreasing subseq ending at seq[i]
    subseq = [(1,1)] * seqLen
    # Iterate over seq array indices, updating tuples in subseq appropriately. 
    for i in range(0,seqLen):
        subseq[i] = checkPrevious(seq[:i+1],subseq[:i+1])   
    maxtuple = maxIncDec(subseq)
    return maxtuple

# Function maxIncDec returns a 2-tuple with size of longest increasing and decreasing subsequence.
def maxIncDec(subseq):
    print(subseq)
    # Array with indices of increasing subsequences and decreasing subsequences
    maxtuple = [1,1] # Will be returned as a tuple, but since tuples are not mutable, will start it as a list
    for element in subseq:
        maxtuple[0] = max(maxtuple[0], element[0])
        maxtuple[1] = max(maxtuple[1], element[1])
    return tuple(maxtuple) # Returned tuple consists of longest increasing and longest decreasing subsequence.


# Returns a tuple for ith element of seq[i], with first num in tuple indicating the longest increasing subseq, 
# second num in tuple indicating longest decreasing subseq that includes element i. Element i is the last element
# in the list seq that was passed to checkPrevious.
def checkPrevious(seq, subseq):
    length = len(seq)
    maxinc = 0
    maxdec = 0
    for i in range(0,length-1):
        if seq[i] < seq[length - 1]:
            maxinc = max(maxinc, subseq[i][0])
        else:
            maxdec = max(maxdec, subseq[i][1])
    return (maxinc + 1, maxdec + 1)




if __name__ == "__main__":
    main()