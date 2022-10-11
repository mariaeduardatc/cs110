def factorial_iterative_steps(number):

    if number < 0:
        raise ValueError("We cannot compute the factorial of a negative number")
    else:
            ## you will need to make changes to this code block and return statement
        temp = number
        print('hi')
        for i in range(number-1, 1, -1):
            temp *= i
            #print(i, 'hello')
            print('aaa')
        return print(i, number, temp)

factorial_iterative_steps(3)