#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if ord(ch) >= 97 and ord(ch) <= 122:
            print("{:c}".format(ord(ch) - 32))
        else:
            print("{:c}".format(ch))
