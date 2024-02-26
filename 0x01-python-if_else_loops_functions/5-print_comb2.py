#!/usr/bin/python3
for i in range(100):
    if i % 10 == i:
        print("{%02d},".format(i), end=' ')
    else:
        print("{},".format(i), end=' ')
