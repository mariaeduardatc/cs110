def selection_sort(lst):
    '''
    Parameters
    -----------
    lst: list of unsorted integers
    
    Return
    ----------
    lst: list of sorted integers
    '''
    length = len(lst)
    
    for index in range (length):
        minidx = index # minidx will 1st assume 0 
        for curr_index in range(index+1, length):
            if lst[curr_index] < lst[minidx]: # remember curr_index is always i+1
                minidx = curr_index
        # !!! run this on VScode to test why it should be out of the if and for
        (lst[index], lst[minidx]) = (lst[minidx], lst[index])
    return lst