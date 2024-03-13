#!/usr/bin/python3
def print_last_digit(number):
    last_value = abs(number) % 10
    print("{}".format(last_value), end="")
    return abs(last_value)
