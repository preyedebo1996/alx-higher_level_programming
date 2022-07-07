#!/usr/bin/python3
"""Calculator"""

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    args = sys.argv[1:]
    arg_count = len(args)
    if arg_count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(args[0])
        b = int(args[2])
        operator = args[1]
        if operator == '+':
            print("{} {} {} = {}".format(a, operator, b, add(a, b)))
        elif operator == '-':
            print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
        elif operator == '*':
            print("{} {} {} = {}".format(a, operator, b, mul(a, b)))
        elif operator == '/':
            print("{} {} {} = {}".format(a, operator, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
