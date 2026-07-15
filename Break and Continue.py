# n = int(input("Enter the numbers."))

i = 1
total = 0
while i > 0 :
    n = int(input("Enter the numbers."))
    if n == 0:
        break

    if n < 0:
        continue
    
    total = total + n
    print(total)

    i += 1
    
print(total)
