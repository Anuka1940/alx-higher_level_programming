"""module contain a mthod add_integer which return the summatio of two integers "a" and "b"
"""


def add_integer(a, b=98):
    """return summation of int a and int b
    riase TypeError ("a must be an integer)
    """
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    if type(a) not in [int, float]:
        raise TypeError ("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError ("b must be an integer")
    return a + b
