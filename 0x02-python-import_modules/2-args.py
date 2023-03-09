#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    no_of_argv = len(sys.argv) - 1
    if no_of_argv == 1:
        print("{} argument:".format(no_of_argv))
        print("{}: {}".format(no_of_argv, sys.argv[no_of_argv]))
    elif no_of_argv == 0:
        print("{} arguments.".format(no_of_argv))
    elif no_of_argv > 1:
        print("{} arguments:".format(no_of_argv))
        for i in range(1, no_of_argv + 1):
            print("{}: {}".format(i, sys.argv[i]))
