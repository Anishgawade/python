# Write a function to ask a numeber from user and print whether it is even or odd


def odd_even():
    num = int(input("Enter the number"))
    if num % 2 == 0:
        print("Even")
    else :
        print("Odd")


odd_even()