def line_stepper(start, k):
    """
    Complete the function line_stepper, which returns the number of ways there are to go from
    start to 0 on the number line by taking exactly k steps along the number line.

    >>> line_stepper(1, 1)
    1
    >>> line_stepper(0, 2)
    2
    >>> line_stepper(-3, 3)
    1
    >>> line_stepper(3, 5)
    5
    """
    "*** YOUR CODE HERE ***"

    if abs(start) == 1 and k == 1:
        return 1
    elif start != 0 and k < 1:
        return 0
    else:
        return line_stepper(start - 1, k - 1) + line_stepper(start + 1, k - 1)