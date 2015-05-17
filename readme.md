# Python REST proof-of-concept

An experiment using REST between chunks of python code.

[Blog post](http://flyingfisch.github.io/programming/web/2015/05/17/using-rest-internally.html)

## Documentation

~~~python
create(object)
"""
Creates a new object.

Keyword arguments:
object -- Object or list of objects to create
"""

read()
"""Returns a list of created objects."""

update(objectId, object)
"""
Updates object.

Keyword arguments:
objectId -- Key of object to update
object -- Object to update with
"""

delete(objectId)
"""
Deletes object from list.

Keyword arguments:
objectId -- Key of object to delete
"""
~~~
