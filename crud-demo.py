#!/usr/bin/python3

from rest import CRUD

#User class {{{
class User:
    name = ""
    age = 0
    weight = 0

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def __repr__(self):
        return "User {{ name: {0}, age: {1}, weight: {2} }}".format(self.name, self.age, self.weight)
#}}}

# make a collection of users
users = CRUD()

# make some users
joe = User("Joe Smith", 45, 180)
mary = User("Mary Jones", 21, 120)
james = User("James Donovan", 28, 190)
john = User("John Doe", 32, 210)

# add them to users
users.create([joe, mary, james])
print("Users created\r\n", users.read())

# put john in users
users.create(john)
print("Added another\r\n", users.read())

# modify john
john = User("John Doe, Jr.", 32, 210)
users.update(3, john)
print("Updated John\r\n", users.read())

# delete john
users.delete(3)
print("Deleted John\r\n", users.read())
