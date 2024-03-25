#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return None

    Len = len(roman_string)
    Rst = roman_string
    sum = 0
    for i in range(Len):
        if Rst[i] == 'I':
            if (i != Len - 1) and (Rst[i + 1] == 'X' or Rst[i + 1] == 'V'):
                sum = sum - 1
            else:
                sum = sum + 1
        elif Rst[i] == 'V':
            sum = sum + 5
        elif Rst[i] == 'X':
            if (i != Len - 1) and (Rst[i + 1] == 'L' or Rst[i + 1] == 'C'):
                sum = sum - 10
            else:
                sum = sum + 10
        elif Rst[i] == 'L':
            sum = sum + 50
        elif Rst[i] == 'C':
            if (i != Len - 1) and (Rst[i + 1] == 'D' or Rst[i + 1] == 'M'):
                sum = sum - 100
            else:
                sum = sum + 100
        elif Rst[i] == 'D':
            sum = sum + 500
        elif Rst[i] == 'M':
            sum = sum + 1000

    return sum
