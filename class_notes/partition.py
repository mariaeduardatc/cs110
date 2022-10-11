def partition(A,p,r):
    """
    The partition procedure in quicksort, which rearranges the subarray A[p...r] in place.
    Parameters
    ----------
    A : list
    	Length of the input list
    p : int
    	Start point. p>=0
    r: int 
    	End point. r<len(A)
    Returns
    -------
    i+1 : int
    	Index of the pivot
    """
    
    x = A[r]
    i = p-1 # maybe we dont need this part

    for j in range (p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]

    return i+1

A = [1,5,6,2,3,8,9,4,7]
assert partition(A, 0, len(A)-1)==6