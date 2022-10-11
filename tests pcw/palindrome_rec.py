def is_palindrome_recursive(word):
    """
    This function identifies whether a word is a palindrome recursively.

    Parameters
    ----------
    word : str
        Word we wish to check
    
    Returns
    -------
    boolean
        True if input is a palindrome, False otherwise
        
    """
    if type(word) is int:
        word = str(word)
    haha = [i for i in word]
    print(haha)

    if len(haha) > 1:
        if haha[0] == haha[-1]:
            haha.pop(0)
            haha.pop(-1)
            return is_palindrome_recursive(haha)
        if haha[0] != haha[-1]:
            return False

    return True

print(is_palindrome_recursive(1211))

 
