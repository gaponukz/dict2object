from dict2object import Object

user1 = Object({
    "name": "John",
    "age": 18
})

user2 = Object(
    name="Adam",
    age=21,
    job={
        "name": "programmer",
        "experience": 5
    }
)

user3 = Object.load('{"name": "Anna", "age": 20}')

print(user1.name)
print(user2.job.name)
print(user3.name)
print(user1 == user2)

print(user1.to_dict())

for key in user2.keys():
    print(user2[key])
