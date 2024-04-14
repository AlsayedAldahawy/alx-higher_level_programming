#!/usr/bin/python3
print_square = __import__('4-print_square').print_square

print_square(4)
print("")
print_square(10)
print("")
print_square(0)
print("")
print_square(1)
print("")

for i in [-1, 2.5, -.05, "f"]:
    try:
        print_square(i)

    except Exception as e:
        print(e)
    print("")
