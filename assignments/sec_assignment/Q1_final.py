def my_sort(lst): 
    '''
    Return the sorted list.
    Inputs:
    - lst: a list of unsorted numbers
    
    Outputs:
    - lst: a list of sorted numbers
    '''
    n = len(lst)
    piles = []
    # popping the 1st element of the list and simultaneously appending it to piles
    # piles is a list of lists
    piles.append([lst.pop(0)])
    
    while lst:
        # gets the 1st element of the original list
        item = lst.pop(0)
        placed = False

        # pile are the lists inside piles
        for pile in piles:
            if item > pile[-1]:
                # here we would directly append to pile (the list inside piles) -> it would be sorted
                pile.append(item)
                placed = True
                break
        if not placed:
            # if item cannot be appended it means it is not bigger than the one already in pile
            # append in piles
            piles.append([item])

    while len(lst) < n:
        # gets the last elements of each list pile and puts them on the list tops
        tops = [pile[-1] for pile in piles]
        # gets the index of the smallest number in tops
        idx_smallest = tops.index(min(tops))

        # gets the element in piles[idx_smallest][0] and appends it in lst
        lst.append(piles[idx_smallest].pop(0))

        # ASK!!!!!!!
        piles = list(filter(None, piles))
    return lst
