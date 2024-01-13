#!/usr/bin/python3
''' Python's F-String for String Interpolation and Formatting '''


''' the modulo operator %'''
name = 'Sayed'
age = 28
status = "single"
profession = "ECE engineer"
experience = 5
graduation_year = 2019
siblings = 2


'print("Hello, %s!, you are %d" %(name, age))'

print("""Hello, %(n)s!, you are %(a)d yo. \nyou are %(s)s working as %(p)s, with %(x)d years experience. \
\nyou have graduated in %(g)d \nyou have %(sib)d siblings""" %{"n": name, 'a': age, 's': status, 'p':profession, 'x': experience,'sib': siblings, 'g': graduation_year})


