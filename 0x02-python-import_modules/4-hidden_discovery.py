#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    all = dir(hidden_4)
    for i in all:
        if not i.startswith("__"):
            print(i)
