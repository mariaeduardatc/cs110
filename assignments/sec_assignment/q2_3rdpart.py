import random
arr = [random.randrange(-1000, 1000) for _ in range(100)]

def insertion_sort(arr):
    '''
    YOUR DOCSTRING HERE
    '''
    print('INSERTION')
    for j in range (1, len(arr)):
        key = arr[j]
        i = j -1 
        
        while i>=0 and arr[i] > key:
            arr[i+1] = arr[i] 
            i = i-1 
            
        arr[i+1] = key
    
    return arr


def merge(arr, start, q, end):
    print('merge')
    
    L = arr[start:q+1]
    R = arr[q+1:end+1]
    

    L.append(float('inf'))
    R.append(float('inf'))
    
    i = 0 
    j = 0
    
    for k in range(start, end+1):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
            
    return arr   
	

def merge_sort_until_k(arr, start, end, k):
    '''
    YOUR DOCSTRING HERE
    '''
    k = int(k)
    if start < end:
        q = (start+end)//2
        merge_sort_until_k(arr, start, q)
        merge_sort_until_k(arr, q+1, end)
        merge(arr,start,q,end)
        if end > k:
            return insertion_sort(arr)
    
    return arr

    if start+k < end:
        q = (start+end)//2
        # print('1st call merge_sort_until_k')
        merge_sort_until_k(arr, start, q)
        # print(arr, 'after until k 1st call')

        # print('sec call merge_sort_until_k')
        merge_sort_until_k(arr, q+1, end)
        # print(arr, 'after until k 2nd call')

        # print('call merge')
        merge(arr,start,q,end)
        # print(arr, 'after merge')
    else:
        return insertion_sort(arr)

a = [3,3,1,0,3,6,5,4,8,3,6,5,4,8,9,4,5,6,7,3,2,4,6,4,2]
print(merge_sort_until_k(a, 0, len(a)-1))