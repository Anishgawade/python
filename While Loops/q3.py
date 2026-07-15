# Ask a number and give a multiplication table 

n = int(input("Enter the number"))

i = 1

while i <= 10:
    print(f"{n} x {i} = {n*i}")

    i += 1