#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if 'a' <= c <= 'z':
            u_char = chr(ord(c) - 32)
        else:
            u_char = c
        print("{}".format(u_char), end='')
    print()
