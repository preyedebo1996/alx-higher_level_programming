#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    argv = sys.argv[1:]
    len_arg = len(argv)
    count = 1
    if len_arg == 0:
        print("{:d} arguments.".format(len_arg))
    elif len_arg == 1:
        print("{:d} argument:".format(len_arg))
        print("{:d}: {:s}".format(len_arg, argv[1])
    else:
        print("{} arguments:".format(len_arg))
        while count <= len_arg:
            print("{}: ".format(count, argv[count]))
            count++
