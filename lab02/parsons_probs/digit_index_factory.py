
def digit_index_factory(num, k):
    """
    Returns a function that takes no arguments, and outputs the offset
    between k and the rightmost digit of num. If k is not in num, then
    the returned function returns -1. Note that 0 is considered to
    contain no digits (not even 0).
    >>> digit_index_factory(34567, 4)() # .Case 1
    3
    >>> digit_index_factory(30001, 0)() # .Case 2
    1
    >>> digit_index_factory(999, 1)() # .Case 3
    -1
    >>> digit_index_factory(1234, 0)() # .Case 4
    -1
    """
    "*** YOUR CODE HERE ***"
    offset = 0
    flag = 0
    while num != 0:
        if num % 10 != k:
            num //= 10
        else:
            flag = 1
            break

        offset += 1
    
    def f():
        return -1 if flag == 0 else offset

    return f
