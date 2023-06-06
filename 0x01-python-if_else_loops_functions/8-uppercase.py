#!/usr/bin/python3
def uppercase(str):
    for C in str:
        if ord(C) >= ord('a') and ord(C) <= ord('z'):
            char = chr(ord(C) - 32)
        else:
            char = C
        print("{:s}".format(char), end="")
    print('')
