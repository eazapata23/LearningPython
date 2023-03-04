# Dictionaries allow you to create key value pairs

dog = {"name": "Roger", "age": 8, "color": "black"}

# dog["name"] = "Syd"

# print(dog.get("name"))
# print(dog.get("color", "brown"))
# print(dog.pop("name"))

# print(dog.popitem())

# print(dog)

# print("color" in dog)

# print(list(dog.keys()))

# print(dog.values())

# print(list(dog.values()))

# print(list(dog.items())) # coverts everything in the dictionary into a list

dog["favorite food"] = "Chicken"
# print(len(dog))

del dog['color']

dogCopy = dog.copy()

print(dog)
