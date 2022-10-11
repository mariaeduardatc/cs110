    # list com os precos dos stocks
    # cada index eh um dia
    # temos que saber qual a maior diferenca (positiva)
    # comece no primeiro index e faca subtracoes com os outros 
    # (faca comparacoes p essas subtracoes assim vc consegue aramazenar qual a maior)

def bruteforce_max_subarray(array):

    pointer = 0
    maxim = sum(array)
    first_index = 0
    last_index = 0

    while pointer < len(array) -1:  # we don't need to compare the last day since we cant sell anything after the last day
        for price in array:
            if array.index(price) > pointer:
                diff = sum(array[pointer:array.index(price)+1]) # summing the elements from pointer to the the index of the element price

                if diff > maxim:
                    first_index = pointer
                    last_index = array.index(price)
                    maxim = diff
        pointer += 1

    return [first_index, last_index, maxim]

A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

print(bruteforce_max_subarray(A))