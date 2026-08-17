# Write a function find_max that takes 3 numbers as input and prints the largest one

def find_max(a,b,c):
    if a > b and a > c:
        print("a")
    elif b > a and b > c:
        print("b")
    else :
        print("c")
n1 = int(input("Enter the first number:"))
n2 = int(input("Enter the second number:"))
n3 = int(input("Enter the third number:"))

find_max(n1,n2,n3)