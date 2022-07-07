#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    infinite_sum = 0
    for i in range(len(sys.argv) - 1):
        infinite_sum += int(sys.argv[i + 1])
    print("{}".format(infinite_sum))
