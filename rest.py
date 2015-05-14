#!/usr/bin/python3

"""
Using REST between Python blocks
"""

class CRUD:
    _objects = []

    def create(self, object):
        if type(object) == type([]):
            self._objects.extend(object)
        else:
            self._objects.append(object)

    def read(self):
        return self._objects

    def update(self, objectId, object):
        self._objects[objectId] = object

    def delete(self, objectId):
        self._objects.pop(objectId)

