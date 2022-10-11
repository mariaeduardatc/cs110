
def is_palindrome_iterative(word):  
    lst = [i for i in word]
    
    while len(lst) > 1:

        if len(lst) <= 1:
            return True
        else:
            if lst[0] != lst[len(lst) - 1]:
                return False
            
            lst.pop(0)
            lst.pop(-1)
    return True      


print(is_palindrome_iterative('aha'))