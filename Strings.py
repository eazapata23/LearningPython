"Zapa"
# 'Zapa'
# name = "Zapa"
# phrase = "Zapa" + "is my name"
# phrase = name + " is my name"
# name += " is my name"
# print(name)
# age = str(39)

# print(""" Zapa is

# 33

# years old
# """)

# String methods
print("zapa".upper())
print("ZAPA".lower())
print("zAPA person".title())
print("zAPA person".islower())

# list of common string methods - they return a new modified string
# isalpha() to check if a string contains only characters and is not empty
# isalnum() to check if a string contains characters or digits and is not empty
# isdecimal() to check if a string contains digits and is not empty
# lower() to get a lowercase version of a string
# islower() to check if a string is lowercase
# upper() to get an uppercase version of a string
# isupper() to check if a string is uppercase
# title() to get a capitalized version of a string
# startswith() to check if the string starts with a specific substring
# endswith() to check if the string ends with a specific substring
# replace() to replace a part of a string
# split() to split a string on a specific character separator
# strip() to trim the whitespace from a string
# join() to append new letters to a string
# find() to find the position of a substring

name = "Zapa"
print(name.lower())
print(name)
print(len(name))  # gives you the length of the string

# escaping is a special way to add special characters into a string
name = "Za\"pa"  # --> escape the "" inside a string by using a \ character
name = 'Za\npa'  # --> \n means new line
print(name)

# string characters & slicing
name = 'Zapa'
print(name[1])
print(name[1:2])  # -> slicing
