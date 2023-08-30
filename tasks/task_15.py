num: int = int(input("Введите целое положительное число: "))

for i in range(num - 1):
    for j in range(num - i - 1):
        print(end=' ')

    for k in range(2 * i + 1):
        print('*', end='')
    print()

# ----------------

for i in range(num - 1, -1, -1):
    for j in range(num - i - 1):
        print(end=" ")
    for k in range(2 * i + 1):
        print("*", end="")
    print()

