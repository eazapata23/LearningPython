# Sets another data structure they work like tuples but they're not ordered and they're mutable

# Sets work well as mathematical sets
set1 = {"Roger", "Syd"}
set2 = {"Roger"}
# set2 = {"Luna"}

# mod = set1 | set2  # unifies each item in both sets - mod is short for modification

# intersect = set1 & set2 #intersect all the items they have in common
# print(intersect)

# print(list(set1))

# A set cannot have two of the same item

mod = set1 - set2  # - to get the difference between two sets
print(mod)
