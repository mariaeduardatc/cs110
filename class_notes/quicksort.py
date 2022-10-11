def quick_sort(A,p,r):
    """
    Perform quicksort algorithm by dividing array A[p..r] into two (possibly empty) subarrays 
    A[p..q-1] and A[q+1..r].
    
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
    A : list
    	The sorted list
        """
    
    if p<r:
        q = partition(A,p,r)
        quick_sort(A,p,q-1)
        quick_sort(A,q+1,r)

    
    return A

A = [0]
assert(quick_sort(A, 0, 0) == [0])
B = [3,1,2]
assert(quick_sort(B, 0, 2) == [1,2,3])
