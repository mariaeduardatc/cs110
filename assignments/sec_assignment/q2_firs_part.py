import time 
import matplotlib.pyplot as plt
import numpy as np
import random


def insertion_sort(arr):
    '''
    YOUR DOCSTRING HERE
    '''
    print('hello hello')
    for j in range (1, len(arr)):
        key = arr[j]
        i = j -1 
        
        while i>=0 and arr[i] > key:
            arr[i+1] = arr[i] 
            i = i-1 
            
        arr[i+1] = key
    
    return arr


def merge(arr, start, q, end):
    
    print('merge merge')
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
	

def merge_sort_until_k(arr, start, end, k=10):
    '''
    YOUR DOCSTRING HERE
    '''
    k = int(k)
    if start+k < end:
        # print('merge_sort_until_k loop start')
        # print(arr)

        q = (start+end)//2
        print(q)
        print(arr)
        print('start', start)
        # print('1st call merge_sort_until_k')
        merge_sort_until_k(arr, start, q, k)
        # print(arr, 'after until k 1st call')

        # print('sec call merge_sort_until_k')
        merge_sort_until_k(arr, q+1, end, k)
        # print(arr, 'after until k 2nd call')

        # print('call merge')
        merge(arr,start,q,end)
        # print(arr, 'after merge')
    else:
        return insertion_sort(arr)
    
    return arr


# arr_2 = [3, 1, 4, 5, 7, 8, 45,2,3,4,56,7,4,12, 75, 44, 7, 0, 63, 11, 33, 28, 810, 8, 3, 1, 4, 5, 7, 8, 45,2,3,4,56,7,4,12, 75, 44, 7, 0, 63, 11, 33, 28, 810, 8, 3, 1, 4, 5, 7, 8, 45,2,3,4,56,7,4,12, 75, 44, 7, 0, 63, 11, 33, 28, 810, 8, 3, 1, 4, 5, 7, 8, 45,2,3,4,56,7,4,12, 75, 44, 7, 0, 63, 11, 33, 28, 810, 8, 3, 1, 4, 5, 7, 8, 45,2,3,4,56,7,4,12, 75, 44, 7, 0, 63, 11, 33, 28, 810, 8, 3, 1, 4, 5, 7, 8, 45,2,3,4,56,7,4,12, 75, 44, 7, 0, 63, 11, 33, 28, 810, 8, 3, 1, 4, 5, 7, 8, 45,2,3,4,56,7,4,12, 75, 44, 7, 0, 63, 11, 33, 28, 810, 8, 3, 1, 4, 5, 7, 8, 45,2,3,4,56,7,4,12, 75, 44, 7, 0, 63, 11, 33, 28, 810, 8,3, 1, 4, 5, 7, 8, 45,2,3,4,56,7,4,12, 75, 44, 7, 0, 63, 11, 33, 28, 810, 8, 3, 1, 4, 5, 7, 8, 45,2,3,4,56,7,4,12, 75, 44, 7, 0, 63, 11, 33, 28, 810, 8, 3, 1, 4, 5, 7, 8, 45,2,3,4,56,7,4,12, 75, 44, 7, 0, 63, 11, 33, 28, 810, 8, 3, 1, 4, 5, 7, 8, 45,2,3,4,56,7,4,12, 75, 44, 7, 0, 63, 11, 33, 28, 810, 8,3, 1, 4, 5, 7, 8, 45,2,3,4,56,7,4,12, 75, 44, 7, 0, 63, 11, 33, 28, 810, 8, 3, 1, 4, 5, 7, 8, 45,2,3,4,56,7,4,12, 75, 44, 7, 0, 63, 11, 33, 28, 810, 8,3, 1, 4, 5, 7, 8, 45,2,3,4,56,7,4,12, 75, 44, 7, 0, 63, 11, 33, 28, 810, 8, 3, 1, 4, 5, 7, 8, 45,2,3,4,56,7,4,12, 75, 44, 7, 0, 63, 11, 33, 28, 810, 8,3, 1, 4, 5, 7, 8, 45,2,3,4,56,7,4,12, 75, 44, 7, 0, 63, 11, 33, 28, 810, 8, 3, 1, 4, 5, 7, 8, 45,2,3,4,56,7,4,12, 75, 44, 7, 0, 63, 11, 33, 28, 810, 8,3, 1, 4, 5, 7, 8, 45,2,3,4,56,7,4,12, 75, 44, 7, 0, 63, 11, 33, 28, 810, 8, 3, 1, 4, 5, 7, 8, 45,2,3,4,56,7,4,12, 75, 44, 7, 0, 63, 11, 33, 28, 810, 8,3, 1, 4, 5, 7, 8, 45,2,3,4,56,7,4,12, 75, 44, 7, 0, 63, 11, 33, 28, 810, 8, 3, 1, 4, 5, 7, 8, 45,2,3,4,56,7,4,12, 75, 44, 7, 0, 63, 11, 33, 28, 810, 8,3, 1, 4, 5, 7, 8, 45,2,3,4,56,7,4,12, 75, 44, 7, 0, 63, 11, 33, 28, 810, 8, 3, 1, 4, 5, 7, 8, 45,2,3,4,56,7,4,12, 75, 44, 7, 0, 63, 11, 33, 28, 810, 8,3, 1, 4, 5, 7, 8, 45,2,3,4,56,7,4,12, 75, 44, 7, 0, 63, 11, 33, 28, 810, 8, 3, 1, 4, 5, 7, 8, 45,2,3,4,56,7,4,12, 75, 44, 7, 0, 63, 11, 33, 28, 810, 8, 3, 1, 4, 5, 7, 8, 45,2,3,4,56,7,4,12, 75, 44, 7, 0, 63, 11, 33, 28, 810, 8, 3, 1, 4, 5, 7, 8, 45,2,3,4,56,7,4,12, 75, 44, 7, 0, 63, 11, 33, 28, 810, 8,3, 1, 4, 5, 7, 8, 45,2,3,4,56,7,4,12, 75, 44, 7, 0, 63, 11, 33, 28, 810, 8, 3, 1, 4, 5, 7, 8, 45,2,3,4,56,7,4,12, 75, 44, 7, 0, 63, 11, 33, 28, 810, 8,3, 1, 4, 5, 7, 8, 45,2,3,4,56,7,4,12, 75, 44, 7, 0, 63, 11, 33, 28, 810, 8, 3, 1, 4, 5, 7, 8, 45,2,3,4,56,7,4,12, 75, 44, 7, 0, 63, 11, 33, 28, 810, 8,3, 1, 4, 5, 7, 8, 45,2,3,4,56,7,4,12, 75, 44, 7, 0, 63, 11, 33, 28, 810, 8, 3, 1, 4, 5, 7, 8, 45,2,3,4,56,7,4,12, 75, 44, 7, 0, 63, 11, 33, 28, 810, 8,3, 1, 4, 5, 7, 8, 45,2,3,4,56,7,4,12, 75, 44, 7, 0, 63, 11, 33, 28, 810, 8, 3, 1, 4, 5, 7, 8, 45,2,3,4,56,7,4,12, 75, 44, 7, 0, 63, 11, 33, 28, 810, 8,3, 1, 4, 5, 7, 8, 45,2,3,4,56,7,4,12, 75, 44, 7, 0, 63, 11, 33, 28, 810, 8, 3, 1, 4, 5, 7, 8, 45,2,3,4,56,7,4,12, 75, 44, 7, 0, 63, 11, 33, 28, 810, 8,3, 1, 4, 5, 7, 8, 45,2,3,4,56,7,4,12, 75, 44, 7, 0, 63, 11, 33, 28, 810, 8, 3, 1, 4, 5, 7, 8, 45,2,3,4,56,7,4,12, 75, 44, 7, 0, 63, 11, 33, 28, 810, 8,3, 1, 4, 5, 7, 8, 45,2,3,4,56,7,4,12, 75, 44, 7, 0, 63, 11, 33, 28, 810, 8, 3, 1, 4, 5, 7, 8, 45,2,3,4,56,7,4,12, 75, 44, 7, 0, 63, 11, 33, 28, 810, 8,3, 1, 4, 5, 7, 8, 45,2,3,4,56,7,4,12, 75, 44, 7, 0, 63, 11, 33, 28, 810, 8, 3, 1, 4, 5, 7, 8, 45,2,3,4,56,7,4,12, 75, 44, 7, 0, 63, 11, 33, 28, 810, 8]
# merge_sort_until_k(arr_2, 0, len(arr_2) - 1)

### runtime merge_sort_until_k
# code based on my PCW and the breakout room Workbook from CS110 Session 10


lst_sizes = np.arange(1, 100, 1)

runtime_merge = []
runtime_insert = []

# number of tests
max_len = 100
num_tests = 50


for lst_size in lst_sizes:
    arr = [random.randint(-100,100) for i in range(lst_size)]
    end_merge = 0 
    end_insert = 0 
    for test in range(num_tests):
        start_merge = time.process_time() 
        merge_sort_until_k(arr, 0, len(arr)-1, k = 10)
        final_merge = time.process_time() - start_merge
        end_merge += final_merge
    runtime_merge.append(end_merge/num_tests)
    
    for test in range(num_tests):
        start_insert = time.process_time() 
        insertion_sort_until_k(arr, 0, len(arr)-1, k = 10)
        final_insert = time.process_time() - start_insert
        end_insert += final_insert
    runtime_insert.append(end_insert/num_tests)



plt.plot(runtime_merge, color="blue",  linewidth=1.0, label="Merge Sort")
plt.title('Experimental analysis of runtime')
plt.xlabel('Input Size')
plt.ylabel('Runtime(s)')

plt.plot(runtime_insert, color="purple",  linewidth=1.0, label="Insertion Sort")
plt.title('Experimental analysis of runtime')
plt.xlabel('Input Size')
plt.ylabel('Runtime(s)')
plt.legend()
plt.show()