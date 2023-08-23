num: int = int(input("Введите целое положительное число: "))

x = 0
while x < num:
    i = 0
    x += 1
    while i < x:
        print(x, end=" ")
        i += 1
    print()

# for i in range(1, num + 1):
#     for j in range(i):
#         print(i, end=" ")
#     print()
