#!/usr/bin/python3
""" Roman to Integer test file
"""
roman_to_int = __import__('12-roman_to_int').roman_to_int

roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "MMXXIII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
roman_number = "MCMXCIV"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
roman_number = "CM"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
roman_number = "DCC"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
roman_number = "CXXV"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
roman_number = "XC"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
roman_number = "LXIV"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
roman_number = "XLVIII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
roman_number = "XXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
roman_number = "MMMCMXCIX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
