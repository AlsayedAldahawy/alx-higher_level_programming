#!/usr/bin/python3
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age

# Example usage
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Compare instances
print(person1 == person2)  # False (not equal)
print(person1 < person2)   # False (not less than)
print(person1 > person2)   # True (greater than)

# You can also use <=, >=, etc.
