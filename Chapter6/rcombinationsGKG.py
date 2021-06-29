from recursion_tree_plotter import plot_recursion_tree

@plot_recursion_tree
def CombinationRepetitionUtil(chosen, arr, index, r, start, end):
    # Current combination is ready,
	# print it
    if index == r:
        #print(f"In first if with/ CRU(chosen={chosen}, arr={arr}, index={index}, r={r}, start={start}, end={end})")
        #input(f"In 1st 'if' index == r: {index}=={r}. About to print chosen(range({r}), then return")
        for j in range(r):
            print(chosen[j], end = " ")
        print()
        return
    # When no more elements are
    # there to put in chosen[]
    if start > n:
        #print(f"In 2nd if w/ CRU(chosen={chosen}, arr={arr}, index={index}, r={r}, start={start}, end={end})")
        #input(f"2nd if, start>n: {start}>{n}. then return")
        return
    # Current is included, put
    # next at next location
    #print(f"In main w/ CRU(chosen={chosen}, arr={arr}, index={index}, r={r}, start={start}, end={end})")
    #input(f"About to update chosen[{index}] to arr[{start}]={arr[start]}")
    chosen[index] = arr[start]
    #input(f"Chosen updated:{chosen}")
								
    # Current is excluded, replace it,
    # with next (Note that i+1 is passed,
    # but index is not changed)
    #print(f"Before first recursive call:in CRU(chosen={chosen}, arr={arr}, index={index}, r={r}, start={start}, end={end})")
    #input(f"About to call CRU(chosen={chosen}, arr={arr}, index ={index + 1}, r={r}, start={start}, end={end})")
    CombinationRepetitionUtil(chosen, arr, index + 1, r, start, end)
    #print(f"Before second recursive call In CRU(chosen={chosen}, arr={arr}, index={index}, r={r}, start={start}, end={end})")
    #input(f"About to call CRU(chosen={chosen}, arr={arr}, index ={index}, r={r}, start={start+1}, end={end})")
    CombinationRepetitionUtil(chosen, arr, index, r, start + 1, end)
	
            

# The main function that prints all
# combinations of size r in arr[] of
# size n. This function mainly uses
# CombinationRepetitionUtil()
def CombinationRepetition(arr, n, r):
    # A temporary array to store
    # all combination one by one
    chosen = [0] * r

	# Print all combination using
	# temporary array 'chosen[]'
    #input(f"Initial call to CRU(chosen={chosen}, arr={arr} , index={0}, r={r}, start=0, end={n})")
    CombinationRepetitionUtil(chosen, arr, 0, r, 0, n)

# Driver code
arr = [1, 2, 3, 4]
r = 3
n = len(arr) - 1
CombinationRepetition(arr, n, r)