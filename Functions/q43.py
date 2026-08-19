# Write a function called absolute_value that takes a number and returns its absolute value without
# making use of any built-in function.

def absolute_value(num):
    if num > 0:
        return num
    return num * -1

print(absolute_value(10))
print(absolute_value(-10))
print(absolute_value(-134))


