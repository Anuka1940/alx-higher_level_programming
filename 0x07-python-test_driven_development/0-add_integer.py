"""module to calculate summation
    this module contains on funtion add_integer
    this funtions accepts two arguments a and b,
    these arguments must be int or floats only
    it returns int always
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
