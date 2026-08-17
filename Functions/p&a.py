# # Write a programt to take 3 input integers and return their sum

# def add(a,b,c):
#     print(f"Total is {a+b+c}")

# add(2,4,6)

# Write a program take name , gender and age as input 

def intro(name , age , gender):
    print(f"hey {name}, your age is {age}, and your gender is {gender}")

# intro("Anish",22,"Male")
n = input("Enter your name: ")
a = int(input("Enter your age: "))
g = input("Enter your gender: ")

intro(n, a ,g)
