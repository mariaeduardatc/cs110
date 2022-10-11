
def strobogrammatic_iterative(n):
    '''
    Return all the strobogrammatic numbers that are of length n through recursive
    approach
    ------------
    Parameters:
    n: int
        The targeted length of the digit 
    ------------
    Returns: list
        All strobogrammatic numbers that are of the targeted length
    '''

    numbers_list = []
    step = 0

    # generate range of number with lenght n
    for number in range(10**(n-1), (10**(n)-1)):
        # transform it into a str so we can iterate trough it
        number_str = str(number)

        # don't do nothing if the number has a non-strob. number
        if '2' in number_str or '3' in number_str or '4' in number_str or '5' in number_str or '7' in number_str: 
            pass
        else:
            # transform each character of a number in an element of a list
            number_array = list(number_str)

            step += 1
            
            length = len(number_array)
            counter = 0

            # iterating trough the number
            while counter < length:

                # checking if the number starts and ends with its correspondent
                if number_array[0] == '0' and number_array[-1] == '0'or number_array[0] == '1' and number_array[-1] == '1' or number_array[0] == '8' and number_array[-1] == '8' or number_array[0] == '9' and number_array[-1] == '6' or number_array[0] == '6' and number_array[-1] == '9':
                    holder = number_str
                    step += 1

                    # checking if the number has only one character after possible .pop()
                    if len(number_array) == 1:
                        step += 1
                        # checking if is strob.
                        if number_array[0] == '0' or number_array[0] == '1' or number_array[0] == '8':
                            numbers_list.append(holder)
                            counter += length # done with the checking
                        else:
                            counter += length
                            
                    # checking if the number has two characters after possible .pop()
                    elif len(number_array) == 2:
                        step += 1
                        # checking if after possible .pop() teh number is strob.
                        if number_array[0] + number_array[1] == '69' or number_array[0] + number_array[1] == '96' or number_array[0] + number_array[1] == '88' or number_array[0] + number_array[1] == '11' or number_array[0] + number_array[1] == '00':
                            numbers_list.append(holder) # here is strob
                            counter += length # done with checking
                        else:
                            counter += length
                    
                    #### .POP() ####
                    # if the number has the same character at its beginning and end or 9 and 6 in exchanged 1st and last positions
                    # we can pop those numbers from the list and proceed to check the others in the middle of the number
                    else:
                        step += 1
                        number_array.pop(0)
                        number_array.pop(-1)
                        counter += 1
                else:
                    step += 1
                    counter += length


    
   
    return numbers_list
