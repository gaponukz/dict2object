dict2object
====

dict2object is a dictionary that supports attribute-style access, a la JavaScript.
```py
>>> user = Object({
...     "name": "John",
...     "age": 18,
...     "job": {
...         "name": "programmer",
...         "experience": 5
...     }
... })
>>> user.name
'Jhon'
>>> user.job.name
'programmer'
```
Dictionary Methods
------------------

A dict2object is a subclass of ``dict``; it supports all the methods a ``dict`` does:

````py
>>> user.keys()
['name', 'age', 'job']
````

Serialization
-------------

Bunches happily and transparently serialize from JSON.

````py
>>> user = Object.load('{"name": "Anna", "age": 20}')
>>> user.name
'Anna'
````
