def insertion_sort(A):
    '''
    
    '''
    for j in range (1, len(A)):
        key = A[j] # key will start at the 2nd index
        i = j -1 # ranges index - 1 -> for the first case i = 0
        print('i',i)
        print('A', A)
        print("A[j]", A[j])
        
        # if A[i] > A[j] then do the loop
        while i>=0 and A[i] > key:
            # the swapping is happening here
            A[i+1] = A[i] # A[i+1] is another way of writing A[j]
            i = i-1 # when it gets negative it means that there is no more swapping to do
            # for cases in which the smallest number is the last one to be sorted this i will start a number slightly bigger than 0, 
            # because it is assuming the index of the numbers before this smallest one
            print('hi', i)
        
        # if nothing happens then A[i+1] continues to be A[j]
        A[i+1] = key
    
    return A


insertion_sort([3,2,6,1])