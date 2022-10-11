def bubble_sort(A):
    '''
    Parameters
    --------------
    A: list with unsorted integers
    
    Returns
    --------------
    A: sorted list
    '''
    
    # the following comments are more for a study purpose
    
    # i is the number of sorted elements
    for i in range(len(A)):
        
        # the -1 is so we don't get out of range when we do j+1
        # the i is here so we don't check the indexes that already contain sorted numbers
        for j in range(len(A) - i -1):
            if A[j] > A[j+1]:
                holder = A[j]
                A[j] = A[j+1]
                A[j+1] = holder
    return A

print(bubble_sort([3,2,1,4,5]))