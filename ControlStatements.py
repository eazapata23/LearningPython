# control statement is like a if statement
condition = True

if condition == True:
    print("The condition")
    print("was true")

# print("outside if")

if condition == False:
    print("The condition")
    print("was true")
else:
    print("The condition")
    print("was False")

condition = False
name = "Izzy"

if condition == True:
    print("The condition")
    print("was True")
elif name == "Wavy":
    print("Hello Wavy")
elif name == "Syd":
    print("Hello Syd")
elif name == "Flavio":
    print("Hello Flavio")
else:
    print("The condition")
    print("was False")
