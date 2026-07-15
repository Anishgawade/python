# Sum of all number form 1 - 100 which are divisble by 2 and 7

i = 1 
total = 0

while i <= 100:
    if i % 2 == 0 and i % 7 == 0:
        total = total + i
    i += 1

print(f"Total sum is {total}")