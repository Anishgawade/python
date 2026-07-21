# # 1 2 3 4
# # 1 2 3
# # 1 2
# # 1
# n = int(input("Enter the number:")) #4

# for i in range(1, n+1):
#     for j in range(1, n-i+1):
#         print(j, end=" ")
#     print()
# # Long method used extra variable

# without using n

for i in range(5, 0, -1):
    for j in range(1, i):
        print(j, end=" ")
    print()