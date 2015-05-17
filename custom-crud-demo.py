#!/usr/bin/python3

from rest import CRUD

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

class Users(CRUD):
    def create(self, object):
        print("Custom create method")

    def read(self):
        print("Custom read method")

    def update(self, objectId, object):
        print("Custom update method")

    def delete(self, objectId):
        print("Custom delete method")

users = Users()

joe = User("Joe", 16, 180)

users.create(joe)
users.read()
users.update(0, joe)
users.delete(0)
