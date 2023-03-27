#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        Inside_result = a/b
        return Inside_result
    except ZeroDivisionError:
        Inside_result = None
    finally:
        print("Inside result: {}".format(Inside_result))
