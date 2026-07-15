# Print the factor of the number from the input given
n = int(input("Enter the number : "))
i = 1

print(f"The factor of {n} are : ")

while i <= n:
    if n % i == 0:
        print(i)
    i += 1