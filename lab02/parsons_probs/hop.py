from tkinter import Y


def hop():
    """
    Calling hop returns a curried version of the function f(x, y) = y.
    >>> hop()(3)(2) # .Case 1
    2
    >>> hop()(3)(7) # .Case 2
    7
    >>> hop()(4)(7) # .Case 3
    7
    """
    "*** YOUR CODE HERE ***"
    # solution 1: lambda
    # return lambda x: lambda y: y

    # solution 2: functional programming
    def f(x):
        def g(y):
            return y
        return g
    return f
