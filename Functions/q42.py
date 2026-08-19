# Write a function that called min_of_three that take three numbers and returns the smallest
# without using any built-in function.

def min_of_three(a,b,c):
    if a < b and a < c:
        return ("a")
    elif b < a and b < c:
        return("b")
    return("c")

print(min_of_three(12,23,4))