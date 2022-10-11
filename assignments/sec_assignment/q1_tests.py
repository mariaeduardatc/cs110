
def my_sort(lst): 
    n = len(lst)
    piles = []
    piles.append([lst.pop(0)])
    
    while lst:
        item = lst.pop(0)
        placed = False
        for pile in piles:
            if item > pile[-1]:
                pile.append(item)
                placed = True
                break
        if not placed:
            piles.append([item])

    while len(lst) < n:
        tops = [pile[-1] for pile in piles]
        idx_smallest = tops.index(min(tops))
        lst.append(piles[idx_smallest].pop(0))
        piles = list(filter(None, piles))
    return lst



print(my_sort([8, 5, 7]), 'first')

print(my_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), 'second')