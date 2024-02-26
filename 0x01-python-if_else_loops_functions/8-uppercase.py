#!/usr/bin/python3
def uppercase(str):
    for a in range(len(str)):
        if ord(str[a]) >= 97 and ord(str[a]) <= 122:
            s = 32
        else:
            s = 0
        print("{}".format(chr(ord(str[a]) - s)), end="")
    print("")
