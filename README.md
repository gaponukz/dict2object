# dict2object

**dict2object** is a dictionary that supports attribute-style access, a la JavaScript

[![PyPI version](https://badge.fury.io/py/dict2object-gaponukz.svg)](https://badge.fury.io/py/dict2object-gaponukz)
[![downloads](https://img.shields.io/pypi/dm/dict2object-gaponukz.svg)](https://pypistats.org/packages/dict2object-gaponukz)
[![license](https://img.shields.io/github/license/gaponukz/dict2object.svg)](https://github.com/gaponukz/dict2object/blob/main/LICENSE)

Install
```bash
pip install dict2object-gaponukz
```

Use
```py
from dict2object.dict2object import Object

user1 = Object(
    name="Adam",
    age = 18,
)

user2 = Object({
    "name": "Max",
    "age": 18,
    "job": {
        "name": "developer",
        "experience": 3
    }
})

user3 = user2.copy()
user3.job.name = "full stack developer"

print(user3)

user4 = Object.load('{"name": "Anna", "age": 20}')
user4.job = user3.job

print(user4)
```

## Requirements

* python >= 3.8

You can use `dict2object` with python 3.8. 