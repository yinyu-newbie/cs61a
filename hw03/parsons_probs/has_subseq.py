def has_subseq(n, seq):
    """
    Complete has_subseq, a function which takes in a number n and a "sequence"
    of digits seq and returns whether n contains seq as a subsequence, which
    does not have to be consecutive.

    >>> has_subseq(123, 12)
    True
    >>> has_subseq(141, 11)
    True
    >>> has_subseq(144, 12)
    False
    >>> has_subseq(144, 1441)
    False
    >>> has_subseq(1343412, 134)
    True
    >>> has_subseq(100, 10)
    True
    """
    "*** YOUR CODE HERE ***"

    if n == seq:
        return True

    right_digit_of_seq = seq % 10

    while n > 0:
        right_digit_of_n = n % 10

        if right_digit_of_n == right_digit_of_seq:
            return has_subseq(n//10, seq//10)

        n //= 10
    
    return False