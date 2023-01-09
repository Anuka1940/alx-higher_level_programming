#!/usr/bin/python3
def replace_in_list(my_list, idx, element):

    if (idx < 0):
        return (my_list[idx])
    elif (idx >= len(my_list)):
        return (my_list[idx])
    else:
        my_list[idx] = element
        return (my_list)
