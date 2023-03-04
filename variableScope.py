# variable scope

# age = 8  # global variable | it was declared before a function so we can access it inside a function

# def test():
#     print(age)

# print(age)  # 8
# test()  # 8


def test():
    age = 8  # declaring a variable inside a function = a local variable -> only visible inside a function
    print(age)


test()
