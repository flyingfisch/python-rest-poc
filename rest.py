#!/usr/bin/python3

"""Classes for using REST inside Python programs"""

class CRUD:
    """Class with built-in CRUD functions."""

    _objects = []

    def create(self, object):
        """
        Creates a new object.

        Keyword arguments:
        object -- Object or list of objects to create
        """
        if type(object) == type([]):
            self._objects.extend(object)
        else:
            self._objects.append(object)

    def read(self):
        """Returns a list of created objects."""
        return self._objects

    def update(self, objectId, object):
        """
        Updates object.

        Keyword arguments:
        objectId -- Key of object to update
        object -- Object to update with
        """
        self._objects[objectId] = object

    def delete(self, objectId):
        """
        Deletes object from list.

        Keyword arguments:
        objectId -- Key of object to delete
        """
        self._objects.pop(objectId)
