num: int = int(input("Введите целое положительное число: "))

for i in range(num - 1):
    for j in range(num - i - 1):
        print(end=' ')
    for k in range(2 * i + 1):
        print('*', end='')  # Придерживайтесь одному стилю,
        # либо одинарные,
        # либо двойные кавычки в программе
    print()

for i in range(num - 1, -1, -1):
    for j in range(num - i - 1):
        print(end=" ")
    for k in range(2 * i + 1):
        print("*", end="")
    print()

# -----------------------------------

# TODO: Решение через while
