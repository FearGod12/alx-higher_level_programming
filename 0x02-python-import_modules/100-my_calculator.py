#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    n = len(argv)
    if n != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    opr = argv[2]
    a = int(argv[1])
    b = int(argv[3])
    if opr == "+":
        print("{} {} {} = {}".format(a, opr, b,  add(a, b)))
    elif opr == "-":
        print("{} {} {} = {}".format(a, opr, b,  sub(a, b)))
    elif opr == "*":
        print("{} {} {} = {}".format(a, opr, b,  mul(a, b)))
    elif opr == "/":
        print("{} {} {} = {}".format(a, opr, b,  div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
