num: int = int(input("Введите целое положительное число: "))
#
# counter: int = 1
# for i in range(1, num + 1):
#     for j in range(i):
#         print(counter, end=" ")
#         counter += 1
#     print()
counter: int = 1
i: int = 0
while i < num:
    i += 1
    j: int = 0
    while j < i:
        print(counter, end=" ")
        j += 1
        counter += 1
    print()
