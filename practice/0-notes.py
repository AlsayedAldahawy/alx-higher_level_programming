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

print('''----the modulo operator % Method----''')

'print("Hello, %s!, you are %d" %(name, age))'

print("""Hello, %(n)s!, you are %(a)d yo. \nyou are %(s)s working as %(p)s, with %(x)d years experience. \
\nyou have graduated in %(g)d \nyou have %(sib)d siblings""" %{"n": name, 'a': age, 's': status, 'p':profession, 'x': experience,'sib': siblings, 'g': graduation_year})


print('''----The str.format() Method----''')
print("""Hello, {}!, you are {} yo. \nyou are {} working as {}, with {} years experience. \
\nyou have graduated in {} \nyou have {} siblings""".format(name, age, status, profession, experience, graduation_year, siblings))
print()
print("/*/*using dictionaries/*/*")

person = {"name": "Hamada", "age": 28, "job":"an engineer"}

print("Hi {name}!, you are {age} years old, you are working as {job}".format(**person))
