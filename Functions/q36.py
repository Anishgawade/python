# Write a function that prints all the factors of the numbers entered by the user

def factors():
    num = int(input("Enter the number:"))
    for i in range(1, num+1):
        if num % i == 0:
            print(i, end=" ")

factors()