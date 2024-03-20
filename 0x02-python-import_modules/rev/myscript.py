#!/usr/bin/python3


def say_hello():
    print("Hello from my_script!")

if __name__ == "__main__":
    # This block will execute only if my_script.py is run directly
    print("Running my_script directly")
    say_hello()
else:
    # This block will execute if my_script.py is imported as a module
    print("Imported my_script as a module")
