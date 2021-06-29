# chapter 9, Computer Project 8: Given an n-ary relation, find the projection of 
# this relation when specified fields are deleted.
# Input format for n-ary relation: Suppose we have a relation consisting of
# (Student_name, ID_number, Major, GPA). One relation representing the data
# (Ackermann, 231455, Computer Science, 3.88) will be represented in memory as 
# a dictionary: {"Student_name":"Ackermann", "ID_number":231455, "Major":"Computer Science",
# "GPA":3.88}


def main():
    # Input - Represent N-ary relation as a dict
    inputDict = {"Student_name":"Ackermann", "ID_number":231455, "Major":"Computer Science","GPA":3.88}
    fieldsToDelete =["ID_number", "Major"]

    # Output
    print(projection(inputDict, fieldsToDelete))
    print(inputDict) # Test to make sure inputDict is unchanged.



def projection(inputDict, fieldsToDelete):
    newDict = inputDict.copy()
    for field in fieldsToDelete:
        del newDict[field]
    return newDict


if __name__ == "__main__":
    main()