#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv_c = len(sys.argv) - 1
    total = 0
    for n in range(1, argv_c + 1):
        total += int(sys.argv[n])
    print(total)
