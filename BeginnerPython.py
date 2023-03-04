name = "zapa"  # this is an inline comment
print(type(name) == str)
print(isinstance(name, str))

age = 2
print(isinstance(age, int))

age = int("20")
print(isinstance(age, int))

number = "20"
age = int(number)
print(isinstance(age, int))  # casting

# this is a commented line
# everything indented belongs to a block like a control statement, conditional block or a function or a class

# complex for complex numbers
# bool for booleans
# list for lists
# tuple for tuples
# range for ranges
# dict for dictionaries
# set for sets

# operators
# arithmetic operators
# 1 + 1 2
# 2 - 1 1
# 2 * 2 4
# 4 / 2 2
# 4 % 3 1
# 4 ** 2 16 **-> exponents
# 5 // 2 2 // -> floor division does division then rounds down to the nearest whole number

age = 8
age += 8  # age = age + 8
print(age)

# comparison operators
# a = 1 assignment operator
# b = 2 assignment operator
# a == b False
# a != b True
# a > b False
# a <= b True

# boolean operators
# condition1 = True
# conditon2 = False

# not condition1 False
# condition1 and condition2 False
# condition 1 or condition2 True

# or operator -> if x is false then y else x
# print(0 or 1) 1
# print(False or 'hey') 'hey'
# print('hi' or 'hey') 'hi'
# print([] or False) 'False'
# print(False or []) '[]'

# and operator -> if x is false then y else y
# print(0 and 1) 0
# print(1 and 0) 0
# print(False and 'hey') False
# print('hi' and 'hey') 'hey'
# print([] and False) []
# print(False and []) False

# ternary operator allows you to quickly define a conditional
# def is_adult(age): ---> slow way to do it without a ternary
#     if age > 18:
#         return True
#     else:
#         return False

# def is_adult2(age):
#     return True if age > 18 else False --> basically an if else all on a single line
