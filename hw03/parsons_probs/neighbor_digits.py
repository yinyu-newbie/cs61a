from turtle import right


def neighbor_digits(num, prev_digit=-1):
    """
    Returns the number of digits in num that have the same digit to its right
    or left.
    >>> neighbor_digits(111)
    3
    >>> neighbor_digits(123)
    0
    >>> neighbor_digits(112)
    2
    >>> neighbor_digits(1122)
    4
    """
    "*** YOUR CODE HERE ***"

    if num < 10:
        return 1 if num == prev_digit else 0

    else:
        rightmost_num = num % 10
        num //= 10

        if rightmost_num != prev_digit:
            if num % 10 == rightmost_num:  # update prev_digit with the same digit
                return 1 + neighbor_digits(num, rightmost_num)
            else:                          # update prev_digit with lonely digit
                return neighbor_digits(num, rightmost_num)
        else:                              # check digit same with prev_digit
            return 1 + neighbor_digits(num, prev_digit)