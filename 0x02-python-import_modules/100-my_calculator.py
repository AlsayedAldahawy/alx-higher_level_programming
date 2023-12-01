#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    if __name__ == "__main__":
        argc = len(sys.argv) - 1
        if (argc != 3):
            print("Usage: ./100-my_calculator.py <a> <operator> <b>")
            exit(1)
        i = int(sys.argv[1])
        j = int(sys.argv[3])
        op = sys.argv[2]

        if (op == "+"):
            out = add(i, j)
        elif (op == "-"):
            out = sub(i, j)
        elif (op == "*"):
            out = mul(i, j)
        elif (op == "/"):
            out = div(i, j)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        print("{} {} {} = {}".format(i, op, j, out))
