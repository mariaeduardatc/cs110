
def my_sort(lst): 
    n = len(lst)
    piles = []
    print(lst, 'before pop')
    # popping the 1st element of the list and simultaneously appending it to piles
    piles.append([lst.pop(0)])
    # piles is a list of lists
    print(lst, 'after pop')
    
    while lst:
        # gets the 1st element of the original list
        item = lst.pop(0)
        print(item, 'item')
        placed = False

        # pile are the lists inside piles
        for pile in piles:
            print(pile, 'pile')
            print(piles, 'piles')
            if item > pile[-1]:
                # here we would directly append to pile (the list inside piles) -> it would be sorted
                pile.append(item)
                print('true')
                placed = True
                print(piles, 'after true')
                break
        if not placed:
            print('false')
            # if item cannot be appended it means it is not bigger than the one already in pile
            # append in piles
            piles.append([item])
            print(piles,'test 5')

    while len(lst) < n:
        print('second while')
        # gets the last elements of each list pile and puts them on the list tops
        tops = [pile[-1] for pile in piles]
        print(tops, 'tops')
        # gets the index of the smallest number in tops
        idx_smallest = tops.index(min(tops))
        print(idx_smallest, 'small index')
        print(piles, 'piles', lst, 'list')

        print(piles[idx_smallest], 'HAHAHA')
        # print(piles[idx_smallest].pop(0), 'HEEELP')

        # gets the element in piles[idx_smallest][0] and appends it in lst
        lst.append(piles[idx_smallest].pop(0))
        print(piles, 'piles sec', lst, 'list sec')

        # ASK!!!!!!!
        piles = list(filter(None, piles))
        print('FINAL', piles)
    return lst



print(my_sort([8, 5, 8]), 'final')