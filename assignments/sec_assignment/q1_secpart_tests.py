def my_sort(lst): 
    '''
    Return the sorted list.
    Inputs:
    - lst: a list of unsorted numbers
    
    Outputs:
    - lst: a list of sorted numbers
    '''
    n = len(lst)
    
    # CHANGE HERE!!!!
    # if my list has no numbers or only one I don't need to sort it
    if n == 0 or n == 1:
        return lst
    
    piles = []
    # takes out the 1st number of the list and simultaneously puts it to piles
    # piles is a list containing other lists
    piles.append([lst.pop(0)])
    
    
    while lst:
        # item gets the 1st number of the original list
        item = lst.pop(0)
        placed = False

        # pile are the lists inside piles
        for pile in piles:
            if item > pile[-1]:
                # put item directly into the end of pile in a sorted manner
                pile.append(item)
                placed = True
                break
        if not placed:
            # if item cannot be added to pile it means it is not bigger than the one already in pile 
            # (it would not generate a sorted combination) -> put it in piles, so it is still together with the other numbers
            piles.append([item])

    while len(lst) < n:
        # CHANGE MADE HERE!!!
        # gets the 1st numbers of each list "pile" and puts them on the list tops
        tops = [pile[0] for pile in piles]
        # gets the position of the smallest number in the new list "tops"
        # this index indicates which sublist the smallest element is in piles
        idx_smallest = tops.index(min(tops))

        # the idx_smallest works because each "pile" is already sorted, we need to just put all "pile" together
        # we get then the first element of the "pile" because we know is the smallest
        lst.append(piles[idx_smallest].pop(0))

        # delete empty lists so it does not disturbs the next call of line 47
        piles = list(filter(None, piles))
    return lst
