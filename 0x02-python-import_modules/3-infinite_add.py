#!/bin/python3
if __name__ == "__main__":
    import sys
    argv = int(sys.argv[1:])
    index = 0
    arg_len = len(argv)
    if len(argv) is 0:
        print("0")
    while index <= arg_len:
        total_sum += argv[index]
        index ++
    print("{}".format(total_sum))
