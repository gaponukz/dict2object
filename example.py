from dict2object.dict2object import Object

item1 = Object({
    "user": {
        "name": "Adam",
        "age": 20,
        "phone": "3803754753"
    }
})

item2 = Object.load('''
    {
        "user": {
            "name": "Max",
            "age": 19,
            "phone": "3803754753"
        }
    }
''')

print(item1.user.name)
print(item2.user.name)

item2.user.name = "Anna"
print(item2.user.name)
