num: int = int(input("Введите целое положительное число: "))

# for i in range(num - 1):
#     for j in range(num - i - 1):
#         print(end=' ')
#     for k in range(2 * i + 1):
#         print('*', end='')  # Придерживайтесь одному стилю,
#         # либо одинарные,
#         # либо двойные кавычки в программе
#     print()
#
# for i in range(num - 1, -1, -1):
#     for j in range(num - i - 1):
#         print(end=" ")
#     for k in range(2 * i + 1):
#         print("*", end="")
#     print()
# -----------------------------------

i = 0
while i < num - 1:
    j = 0
    while j < num - i - 1:
        print(end=' ')
        j += 1
    k = 0
    while k < 2 * i + 1:
        print('*', end='')
        k += 1
    print()
    i += 1

i = 0
while i < num:
    j = 0
    while j < num - i - 1:
        print(end=' ')
        j += 1
    k = 0
    while k < 2 * i + 1:
        print('*', end='')
        k += 1
    print()
    i -= 1






