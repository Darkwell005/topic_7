num: int = int(input("Введите целое положительное число: "))

k = 2 * num - 3
for i in range(num, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k += 1
    for j in range(i + 1):
        print("*", end="")
    print()
# ----------------

i = 0
while i < num:
    j = 0
    while j < num - i - 1:
        print(' ', end='')
        j += 1
    k = 0
    while k < 2 * i + 1:
        print('*', end='')
        k += 1
    print()
    i += 1
