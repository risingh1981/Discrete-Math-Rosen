# Given an m-ary relation and an n-ary relation, and a set of
# common fields, find the join of these relations with respect
# to these common fields.

def main():
    # Input
    naryRel = {"Student_name":"Ackermann", "ID_number":231455}
    maryRel = {"ID_number":231455,"Major":"Computer Science","GPA":3.88, "Residence":"Dorm"}
    commonFields = ["ID_number"]

    # Output
    print(joinRel(naryRel,maryRel,commonFields))
    # {'Student_name': 'Ackermann', 'ID_number': 231455, 'Major': 'Computer Science', 'GPA': 3.88, 'Residence': 'Dorm'}


def joinRel(n,m, cf):
    newRel = {}
    for field in cf:
        if n[field] == m[field]:
            for key in n:
                newRel[key] = n[key]
            for key in m:
                newRel[key] = m[key]

    return newRel


if __name__ == "__main__":
    main()