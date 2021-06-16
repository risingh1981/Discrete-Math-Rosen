def index_2d(myList, startx, endx, starty, endy):
    for i in range(startx, endx + 1):
        for j in range(starty,endy + 1):
            if (myList[i][j] != None):
                return (i,j), myList[i][j]
    return None

board = [[None for x in range(8)] for y in range(8)]
board[1][2] = "M"
board[5][6] = 5
index, val = index_2d(board,4,7,4,7)
print(index)
print(val)
print(type(None))
print(type(None) == "NoneType")
