#!/usr/bin/python3
def remove_char_at(str, n):
    s = ""
    for a in range(len(str)):
        if a != n:
            s = s + str[a]
    return s
