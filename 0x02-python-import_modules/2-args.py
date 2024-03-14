#!/usr/bin/python3
import sys

def print_num_of_and_args(args):
    num_of_args = len(args)

    if num_of_args == 0:
        print("0 arguments.")
    elif num_of_args == 1:
        print("1 argument.")
    else:
        print("{} arguments: ".format(num_of_args))

    for i, arguments in enumerate(args, start = 1):
        print(f"{i} : {arguments}")

if __name__ == "__main__":
    args = sys.argv[1:]
    print_num_of_and_args(args)
