def main(): 

    arr = [[None for i in range(8)] for j in range(8)]
    arr[4][4] = "P"
    xs = 4
    xe = 7
    ys = 4
    ye = 7
    half = 2
    filled = index_2d(arr, "P", xs, xe, ys, ye)
    print(f"Filled square: {filled}")
    ptiles = pTile(xs,xe,ys,ye,half,filled)
    print(ptiles)
    
    #for line in arr:
    #    print(line)
  

def pTile(xs,xe,ys,ye,half,filled):
    if ((filled[0]>= xs) and (filled[0] <= (xe - half)) and (filled[1] >= ys) and (filled[1]<=(ye - half))):
        pTile1 = ((xe - half),(ye - half + 1))
        pTile2 = ((xe - half + 1),(ye - half))
        pTile3 = ((xe - half + 1),(ye - half + 1))
    elif ((filled[0]>= xs) and (filled[0] <= (xe - half)) and (filled[1] >= (ye - half + 1)) and (filled[1]<=(ye))):
        pTile1 = ((xe - half),(ye - half))
        pTile2 = ((xe - half + 1),(ye - half))
        pTile3 = ((xe - half + 1),(ye - half + 1))
    elif ((filled[0]>= (xe - half + 1)) and (filled[0] <= (xe)) and (filled[1] >= (ys)) and (filled[1]<=(ye - half))):
        pTile1 = ((xe - half),(ye - half))
        pTile2 = ((xe - half),(ye - half + 1))
        pTile3 = ((xe - half + 1),(ye - half + 1))
    elif ((filled[0]>= (xe - half + 1)) and (filled[0] <= (xe)) and (filled[1] >= (ye - half + 1)) and (filled[1]<=(ye))):
        pTile1 = ((xe - half),(ye - half))
        pTile2 = ((xe - half),(ye - half + 1))
        pTile3 = ((xe - half + 1),(ye - half))
    return pTile1,pTile2,pTile3

def index_2d(myList, v, startx, endx, starty, endy):
    for i in range(startx, endx + 1):
        for j in range(starty,endy + 1):
            if (myList[i][j] == v):
                return i,j
    return None

'''
def recur(n):
    if (n==0):
        
        return
    print(next(itr))
    return recur(n-1,itr)
'''

main()


