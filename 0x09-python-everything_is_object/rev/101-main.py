#!/usr/bin/python3
LockedClass = __import__('101-locked_class').LockedClass

lc = LockedClass()
lc.first_name = "John"
try:
    print(lc.__dict__)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
