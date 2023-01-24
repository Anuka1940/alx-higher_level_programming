#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0

    for i in range(x):
        if count <= x:
            try:
                print("{}".format(my_list[i]), end='')
                count += 1

            except IndexError:
                break
    print()
    return (count)
