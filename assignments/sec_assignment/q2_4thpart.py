import math
def merge(arr, start, q, end):
    L = arr[start:q+1]
    R = arr[q+1:end+1]
    
    print('error')
    L.append(float('inf'))
    R.append(float('inf'))
    
    i = 0 
    j = 0
    
    for k in range(start, end+1):
        print('oh')
        if L[i] <= R[j]:
            arr[k] = L[i]
        else:
            arr[k] = R[j]
            j += 1
    return arr  

def merge_sort(arr):
    '''
    YOUR DOCSTRING HERE
    '''

    start = 0
    end = len(arr)-1
    
    if start < end:
        q = (start+end)//2
        arr[:q+1] = merge_sort(arr[:q+1])
        arr[q+1:] = merge_sort(arr[q+1:])
        merge(arr,start,q,end)

    
    return arr

def insertion_sort_until_k(arr, start, end):
    '''
    YOUR DOCSTRING HERE
    '''
    k = len(arr)*0.1
    percent = int(k)

    for j in range(start, percent):
        print('teste')
        key = arr[j]
        i = j -1 
        
        while i>=0 and arr[i] > key:
            arr[i+1] = arr[i] 
            i = i-1 
            
        arr[i+1] = key
    
    
    arr[percent:] = merge_sort(arr[percent:])
    merge(arr, 0,  len(arr)-k-1, len(arr)-1)
    return arr

   
    


    
a =  [3, 1, 4, 5, 7, 8, 12, 75, 44, 7, 0, 63, 11, 33, 28, 810, 8]
print(insertion_sort_until_k(a, 0, len(a) - 1))

print(sorted(a), 'sorted')



