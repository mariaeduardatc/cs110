
def first_index (nums, target):
    '''
    Return the start index
    of a target element in a sorted array
    ------------
    Parameters:
    nums: list
        a sorted array
    target: int
        the target value to be found
    ------------
    Returns:
    integer
        first index of the target's occurrence
    '''
    global step
    step = 0
    pointer_beg = 0
    pointer_end = len(nums) - 1

    # check if the list if empty, or if the number is not in the list
    if len(nums) == 0 or nums[pointer_beg] > target or nums[pointer_end] < target:
            step += 1
            return None, step
    # find first index
    else:
        if nums[0] == target:
            step += 1
            return 0
        # if the target is not on the first index of the list the code will examine the list again from the second index inwards
        else:
            step += 1
            recall = first_index(nums[1:], target)
            # if the number does not exist but the 1st number on the list is smaller than it and the last one is bigger
            if recall != None:
                recall = recall + 1
            else:
                step += 1
                return None, step

    return recall

def last_index(nums, target):
    '''
    Return the end index
    of a target element in a sorted array
    ------------
    Parameters:
    nums: list
        a sorted array
    target: int
        the target value to be found
    ------------
    Returns:
    integer
        last index of the target's occurrence
    '''
    step = 0 
    pointer_beg = 0
    pointer_end = len(nums) - 1

    # check if the list if empty, or if the number is not in the list
    if len(nums) == 0 or nums[pointer_beg] > target or nums[pointer_end] < target:
            step += 1
            return None, step
    # find last index
    else:
        step += 1
        if nums[-1] == target:
            return len(nums)-1
        # if the target is not on the first index of the list the code will examine the list again from the second index inwards
        else:
            recall = last_index(nums[:-1], target)
            
    return recall



def recursive_binary_search_extension(nums, target):
    '''
    Return the start and end index (inclusively)
    of a target element in a sorted array
    ------------
    Parameters:
    nums: list
        a sorted array
    target: int
        the target value to be found
    ------------
    Returns:
    list/ None
        list of the beginning and end index if found, else None
    '''
    step = 0

    # call functions to find first and last index
    first_i = first_index(nums, target)
    last_i = last_index(nums, target)

    # if the functions dont find the number    
    if first_i == None or last_i == None:
        step += 1
        return None, step

    # calculate amount of occurrences
    amount = last_i - first_i + 1

    # if last and first index are the same
    if last_i - first_i == 0:
        step += 1
        amount = 1
    
    step += 1

    return [first_i, last_i, amount,step]


print(recursive_binary_search_extension([-1, 0,1,1,1,1,2,2,3,3,9,10], 8))