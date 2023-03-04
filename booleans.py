done = True
done = True

print(type(done) == bool)

if done:
    print("yes")
else:
    print("no")

# numbers are always true except for the number 0
# strings are false only when empty

book_1_read = True
book_2_read = False

read_any_book = any([book_1_read, book_2_read])
# The any function it's a global function it returns True if any of the value of the iterable such as a list
# if any of them are True it's going to return True for all of them

ingredients_purchased = True
meal_cooked = False

ready_to_serve = all([ingredients_purchased, meal_cooked])
# The all function is similar but returns True if ALL of the vales are True
