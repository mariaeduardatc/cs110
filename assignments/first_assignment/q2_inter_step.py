def iterative_binary_search_extension(nums, target):
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

    one_time = 0

    amount = 0

    pointer_beg = 0
    pointer_end = len(nums) - 1

    # check if the list if empty, or if the number is not in the list
    if len(nums) == 0 or nums[pointer_beg] > target or nums[pointer_end] < target:
            step += 1
            return None
    else:
        for num in nums:
            step += 1
            # if number is found
            if num == target:
                amount += 1
                # attribute the index of the number only once to first_index
                while one_time < 1:
                    step += 1
                    first_index = nums.index(target)
                    one_time += 1
        # calculate the index for last_index
        last_index = first_index + amount - 1

    return [first_index, last_index, amount, step]

print(iterative_binary_search_extension([1,1,3,4,5,7,10],4))