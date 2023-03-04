dogs = ["Syd", 1, "Mango", True, "Quincy", 7]

dogs[2] = "Beau"
# dogs.append("Judah")
# dogs.extend(["Judah", 5])
dogs += ["Judah", 5]

dogs.remove("Syd")

print(dogs.pop())  # --> pop will remove and return a single item
print(dogs)

# print("Syd" in dogs)
# print("Beau" in dogs)
# print(dogs[2])

items = ["Roger", "Lucky",  "Shaggy"]

items.insert(2, "Test")
print(items)

# to add multiple items to a list you need slices
items[1:1] = ["Test1", "Test2"]
print(items)

# sort a list
items = ["Roger", "bob", "Beau", "Quincy"]
# itemscopy = items[:]
# items.sort(key=str.lower)
# --> sorted is a global variable that creates a new list without modifying the original list
print(sorted(items, key=str.lower))

print(items)
# print(itemscopy)
